# Cloud Safe 
[![Build Status](https://travis-ci.org/wcc526/cloudsafe.png)](https://travis-ci.org/wcc526/cloudsafe) [![Coverage Status](https://coveralls.io/repos/wcc526/cloudsafe/badge.png)](https://coveralls.io/r/wcc526/cloudsafe)
==================

基于golismero的云安全扫描平台
this is the web ui for the golismero,bug scan
you can see it from https://github.com/golismero/golismero

this web ui is write by django,only need python environment
but the scan tools is basic golismero,make sure you are qualified ,like install
nmap,sqlmap and so on,the os system is kali or backtrack is better!

What's it look like?
===================

The basic login ui like:
![image](https://github.com/wcc526/csenv/raw/master/screenshots/login.png)
The results like:
![image](https://github.com/wcc526/csenv/raw/master/screenshots/results.png)
The admin like:
![image](https://github.com/wcc526/csenv/raw/master/screenshots/admin.png)
The report1 like:
![image](https://github.com/wcc526/csenv/raw/master/screenshots/report1.png)
The report2 like:
![image](https://github.com/wcc526/csenv/raw/master/screenshots/report2.png)
The scan queue like:
![image](https://github.com/wcc526/csenv/raw/master/screenshots/queue.png)

How to use it?
===================
make sure you have install virtualenv,pip,
git clone https://github.com/wcc526/csenv.git

1.run . csenv/bin/activate
2.cd csenv/cloudsafe
3.python manage.py runserver 0.0.0.0:80

The basic username is root,password is toor

enjoy it!

What will be the next features?
====================
I will add more functions,like:

-more powerful report for the statistics
-now the basic language is chinese,I will support english,spanlish
-and so on


[![Bitdeli Badge](https://d2weczhvl823v0.cloudfront.net/wcc526/cloudsafe/trend.png)](https://bitdeli.com/free "Bitdeli Badge")

