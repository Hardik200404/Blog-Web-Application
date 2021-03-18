from django.db.models.signals import post_save
# this will help us send a signal when ever a user is created
#so that we can create a default profile for the user before hand
from django.contrib.auth.models import User#the user will act as the sender of the signal
#now a receiver to receive the signal
from django.dispatch import receiver
#as we will create a default profile,so import profile class
from .models import Profile

@receiver(post_save,sender=User)
def create_profile(sender,instance,created,**kwargs):
    if created:
        Profile.objects.create(user=instance)

#now to save the created profile
@receiver(post_save,sender=User)
def save_profile(sender,instance,**kwargs):
    instance.profile.save()