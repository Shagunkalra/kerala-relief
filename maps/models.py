

# Create your models here.
from django.db import models

from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class Profile(models.Model):
    username = models.OneToOneField(User,on_delete=models.CASCADE)
    
    email = models.EmailField(max_length=30, blank=False)
    password = models.CharField(max_length=15, blank=False)
    amount = models.IntegerField(blank=False)
    Name  =  models.CharField(max_length=15,blank=False)

#@receiver(post_save, sender=User)
#def update_user_profile(sender, instance, created, **kwargs):
 #   if created:
  #      Profile.objects.create(user=instance)
   # instance.profile.save()