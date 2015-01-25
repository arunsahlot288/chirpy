# twitter-clone
A Python(django) based twitter implementation 
-----------------------------
installation  requirements
------------------------------
django 1.7

python 2.7 

mysql 5.5




----------------
Installation
----------------
edit chirpy/setting.py and update database information

Create Database using the name specified in settings.py in mysql

cd chirpy


run command 
	
 ./manage.py syncdb  #sync database
	
 ./manage.py makemigrations  #make migrations 
 
 
 ./manage.py migrate #create tables 
 
 
 ./manage.py runserver #can run on any port defualt 8000


 
 ----------------
Post Installation
----------------
1. Type URL 127.0.0.1:8000

2. You will be directed to a Pre-login page

3. There you can sign up or login 

4. You can See the basic timeline on the Home page

5. In the Popular Accounts you can view all the profiles on the chirpy (twitter clone)

6. In the My Profile section you can see all your posts(chirps) your follower and following users

7. In the Dicover section you can view all the latest posts(chirps)

 




