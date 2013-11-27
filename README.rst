############
Cloud Safe 
############
.. image:: https://api.travis-ci.org/wcc526/cloudsafe.png?branch=master
    :target: http://travis-ci.org/wcc526/cloudsafe
.. image:: https://coveralls.io/repos/wcc526/cloudsafe/badge.png?branch=master
    :target: https://coveralls.io/r/wcc526/cloudsafe
.. image:: https://drone.io/github.com/wcc526/cloudsafe/status.png 
    :target: https://drone.io/github.com/wcc526/cloudsafe/latest

基于golismero的云安全扫描平台
this is the web ui for the golismero,bug scan
you can see it from https://github.com/golismero/golismero

this web ui is write by django,only need python environment
but the scan tools is basic golismero,make sure you are qualified ,like install
nmap,sqlmap and so on,the os system is kali or backtrack is better!

**********
Sceenshots
**********

* The basic login ui like:
.. image:: https://github.com/wcc526/csenv/raw/master/screenshots/login.png
* The results like:
.. image:: https://github.com/wcc526/csenv/raw/master/screenshots/results.png
* The admin like:
.. image:: https://github.com/wcc526/csenv/raw/master/screenshots/admin.png
* The report1 like:
.. image:: https://github.com/wcc526/csenv/raw/master/screenshots/report1.png
* The report2 like:
.. image:: https://github.com/wcc526/csenv/raw/master/screenshots/report2.png
* The scan queue like:
.. image:: https://github.com/wcc526/csenv/raw/master/screenshots/queue.png

**********
How to use it?
**********
make sure you have install virtualenv,pip,
git clone https://github.com/wcc526/csenv.git

* run . csenv/bin/activate
* cd csenv/cloudsafe
* python manage.py runserver 0.0.0.0:80

The basic username is root,password is toor

enjoy it!

**********
Online Group
**********
- QQ群: 260816512

**********
Getting Help
**********
1.IRC channel, #cloudsafe, on irc.freenode.net 
2.email to wcc526@gmail
3.QQ:949409306

**********
What will be the next features?
**********
I will add more functions,like:

* more powerful report for the statistics
* now the basic language is chinese,I will support english,spanlish
* and so on



.. image:: https://d2weczhvl823v0.cloudfront.net/wcc526/cloudsafe/trend.png
   :alt: Bitdeli badge
      :target: https://bitdeli.com/free
