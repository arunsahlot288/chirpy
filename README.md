# twitter-clone
A Python(django) based twitter implementation 
-----------------------------
installation  requirements
------------------------------
django 1.7

python 2.7 

mysql 5.5


please check the patch for wadostuff


----------------
Installation
----------------
edit twitter/setting.py and update database information

Create Database using the name specified in settings.py

cd twitter


run command 
	
 ./manage.py syncdb  #sync database
	
 ./manage.py makemigrations  #make migrations 
 
 
 ./manage.py migrate #create tables 
 
 
 ./manage.py runserver #can run on any port defualt 8000




