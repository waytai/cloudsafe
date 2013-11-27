from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class ihepip(models.Model):
    ip =models.IPAddressField(primary_key=True)
    mac =models.CharField(max_length=200)
    chinesename =models.CharField(max_length=200)
    worktype =models.CharField(max_length=200)
    project =models.CharField(max_length=200)
    phone =models.CharField(max_length=200)
    email =models.EmailField(max_length=95)
    company =models.CharField(max_length=200)
    dept =models.CharField(max_length=200)
    area =models.CharField(max_length=200)
    room =models.CharField(max_length=200)
    period =models.CharField(max_length=200)
    op =models.CharField(max_length=200)
    flag =models.CharField(max_length=200)
    stat =models.CharField(max_length=200)
    def __unicode__(self):
        return self.ip
class ihepresults(models.Model):
    ip =models.ForeignKey(ihepip,related_name="ihepresults_ihepip")
    high =models.BigIntegerField(blank=True)
    mid =models.BigIntegerField(blank=True)
    low =models.BigIntegerField(blank=True)
    info =models.BigIntegerField(blank=True)
    time =models.DateTimeField(auto_now_add=True)
    resultfilepath =models.CharField(max_length=200,primary_key=True)
    taskid =models.CharField(max_length=200,blank=True)
    def chinesename(self):
        return self.ip.chinesename
    def dept(self):
        return self.ip.dept
    def __unicode__(self):
        return self.resultfilepath
class ihepuser(models.Model):
    user =models.OneToOneField(User)
    ip =models.ManyToManyField(ihepip)
    def __unicode__(self):
        return self.user.get_username()
