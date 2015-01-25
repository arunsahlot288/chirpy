from django.db import models
from django.contrib.auth.models import User
import hashlib


class Chirpy(models.Model):    #creating table for storing content of post , user who posted and date 
    content = models.CharField(max_length=140)
    user = models.ForeignKey(User)
    creation_date = models.DateTimeField(auto_now=True, blank=True)

class UserProfile(models.Model):	#table for user information 
    user = models.OneToOneField(User)
    follows = models.ManyToManyField('self', related_name='followed_by', symmetrical=False)

    def gravatar_url(self):     # icon for profile picture
        return "https://lh5.googleusercontent.com/-44zXL7Tz_7g/VI_Rnmu3E5I/AAAAAAAAAss/GbKrH95LDrk/s55-no/twitter.png"

User.profile = property(lambda u: UserProfile.objects.get_or_create(user=u)[0])		#This allows us to fetch the properties of UserProfile easily
