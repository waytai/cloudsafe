# -*- coding: utf-8 -*-
from django.shortcuts import render


import urllib
import urllib2,time

import imaplib
from django.utils import simplejson

import MySQLdb
import sys
import os
import codecs
from django.contrib.auth.models import User
from django.contrib.auth import login,authenticate,logout
from handleui.models import ihepip,ihepuser,ihepresults
from django.http import HttpResponseRedirect

def post(url, data):  
    """
    用来发送post消息
    """
    req = urllib2.Request(url)  
    data = urllib.urlencode(data)  
    opener = urllib2.build_opener(urllib2.HTTPCookieProcessor())  
    response = opener.open(req, data)  
    return response.read()  
def callback(request):
    code=request.GET.get('code') 
    posturl = "https://login.ihep.ac.cn/oauth2/token"  
    data = {'client_id':"***", 'client_secret':"***","grant_type":"authorization_code"
            ,"redirect_uri":"http://cloudsafe.ihep.ac.cn/callback","code":code}  
    ans=post(posturl, data)  
    ans=ans[ans.rfind(r'cstnetId')+13:]
    ans=ans.split(',')[0][:-2]

    user=authenticate(username=ans,password=ans)
    login(request,user)
    user=ihepuser.objects.filter(user=user)[0]
    ip=user.ip.all()
    myip,myemail,myname,myhigh,mymid,mylow,myinfo,mytime,mytaskid=[], [], [], [], [], [], [], [], []
    for i in ip:
        myip.append(str(i))
        ii=ihepip.objects.filter(ip=str(i))[0]
        myemail.append(ii.email)
        myname.append(ii.chinesename)
        r=ihepresults.objects.filter(ip=str(i))
        if len(r)==0:
            myhigh.append(-1)
            mymid.append(-1)
            mylow.append(-1)
            myinfo.append(-1)
            mytime.append(u"未扫描")
            mytaskid.append("")
        else:
            r=r[0]
            myhigh.append(r.high)
            mymid.append(r.mid)
            mylow.append(r.low)
            myinfo.append(r.info)
            mytime.append(r.time)
            mytaskid.append(r.taskid)
    myzip=zip(myip,myemail,myname,myhigh,mymid,mylow,myinfo,mytime,mytaskid)
    return render(request,"handleui/results.html",{'email':request.user.get_username,'myzip':myzip})
def index(request):
    return render(request,"handleui/login.html")
def faq(request):
    return render(request,"handleui/faq.html",{'email':request.user.get_username})
def about(request):
    return render(request,"handleui/about.html",{'email':request.user.get_username})
def chart(request):
    return render(request,"handleui/chart.html")
def advanced(request):
    """
    """
    return render(request,"handleui/advanced.html",{'email':request.user.get_username})
def queue(request):
    user=str(request.user.username)
    user=User.objects.filter(username=user)
    user=ihepuser.objects.filter(user=user)[0]
    ip=user.ip.all()
    myip,myemail,myname,mytaskid=[], [], [], []
    for i in ip:
        myip.append(str(i))
        ii=ihepip.objects.filter(ip=str(i))[0]
        myemail.append(ii.email)
        myname.append(ii.chinesename)
        r=ihepresults.objects.filter(ip=str(i))
        if len(r)==0:
            mytaskid.append("")
        else:
            r=r[0]
            mytaskid.append(r.taskid)
    myzip=zip(myip,myemail,myname,mytaskid)
    return render(request,"handleui/queue.html",{'email':request.user.get_username,'myzip':myzip})
def results(request):
    """
    """
    if request.method == 'POST':
        email=request.POST.get('email','')
        password=request.POST.get('password','')
        try:
            user=authenticate(username=email,password=password)
            login(request,user)
        except Exception,ex:
            return HttpResponseRedirect('/admin')
    elif request.method == 'GET':
         user=request.user

    user=ihepuser.objects.filter(user=user)[0]
    ip=user.ip.all()
    myip,myemail,myname,myhigh,mymid,mylow,myinfo,mytime,mytaskid=[], [], [], [], [], [], [], [], []
    for i in ip:
        myip.append(str(i))
        ii=ihepip.objects.filter(ip=str(i))[0]
        myemail.append(ii.email)
        myname.append(ii.chinesename)
        r=ihepresults.objects.filter(ip=str(i))
        if len(r)==0:
            myhigh.append(-1)
            mymid.append(-1)
            mylow.append(-1)
            myinfo.append(-1)
            mytime.append(u"未扫描")
            mytaskid.append("")
        else:
            r=r[0]
            myhigh.append(r.high)
            mymid.append(r.mid)
            mylow.append(r.low)
            myinfo.append(r.info)
            mytime.append(r.time)
            mytaskid.append(r.taskid)
    myzip=zip(myip,myemail,myname,myhigh,mymid,mylow,myinfo,mytime,mytaskid)
    return render(request,"handleui/results.html",{'email':request.user.get_username,'myzip':myzip})
def getmysql():
    while ihepip.objects.count():
        ihepip.objects.all()[0].delete()
    while ihepuser.objects.count():
        ihepuser.objects.all()[0].delete()
    try:
         conn=MySQLdb.connect(host='****',user='***',passwd='***',db='***',port=3306)
         cur=conn.cursor()
         cur.execute('select ip,mac,name,type,project,phone,email,company,dept,area,room,period,op,flag,stat from secinfo where ip is not null and email is not null;')
         result=cur.fetchall()
         cur.close()
         conn.close()
         ans={}
         for r in result:
             if r[6].endswith('@ihep.ac.cn') or r[6].endswith('@mail.ihep.ac.cn'):
                 mail=r[6].split('@')[0]+'@ihep.ac.cn'
                 #完成ip同步
                 ihepip.objects.get_or_create(ip=str(r[0]).decode('gbk'),
                         mac=str(r[1]).decode('gbk'),
                         chinesename=str(r[2]).decode('gbk'),
                         worktype=str(r[3]).decode('gbk'),
                         project=str(r[4]).decode('gbk'),
                         phone=str(r[5]).decode('gbk'),
                         email=str(mail).decode('gbk'),
                         company=str(r[7]).decode('gbk'),
                         dept=str(r[8]).decode('gbk'),
                         area=str(r[9]).decode('gbk'),
                         room=str(r[10]).decode('gbk'),
                         period=str(r[11]).decode('gbk'),
                         op=str(r[12]).decode('gbk'),
                         flag=str(r[13]).decode('gbk'),
                         stat=str(r[14]).decode('gbk')
                         )
                 #完成用户同步    
                 ans.setdefault(mail,[]).append(r[0])
         for (k,v) in ans.items():
             user=User.objects.filter(username=k)
             if len(user)==0:
                 user=User.objects.create_user(k,k,k)
             else:
                 user=user[0]
             user.save()
             user=ihepuser(user=user)
             user.save()
             for i in v:
                 user.ip.add(i)
             user.save()
    except MySQLdb.Error,e:
         print "Mysql Error %d: %s" % (e.args[0], e.args[1])
def syndatabase(request):
    """
    同步数据库内容
    """

    getmysql()
#    """
    BASE_DIR=os.path.join(os.path.dirname(os.path.dirname(__file__)),'results')
    for root,dirs,files in os.walk(BASE_DIR):
        for name in files:
            fp=open(os.path.join(BASE_DIR,name))
            lines=fp.readlines()
            high,mid,low,info=lines[58].strip()[4:-5],lines[59].strip()[4:-5],lines[60].strip()[4:-5],lines[61].strip()[4:-5]
            fp.close()
            name=name.split('.html')[0]
            ip=ihepip.objects.filter(ip=name)[0]
            if len(ihepresults.objects.filter(ip=ip))==0:
                ihepresults.objects.create(resultfilepath=name,ip=ip,high=high,mid=mid,low=low,info=info,)
            else:
                result=ihepresults.objects.filter(ip=ip)[0]
                result.high=high
                result.mid=mid
                result.low=low
                result.info=info
                result.save()
#    """
    return HttpResponseRedirect('/admin')
