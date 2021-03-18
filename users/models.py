from django.db import models
from django.contrib.auth.models import User
from PIL import Image

class Profile(models.Model):
    #the user should have a one to one relation with the profile and
    #the on_delete value suggests that if the profile is deleted the user will be still there
    #but if the user is deleted the profile should be deleted too
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    image=models.ImageField(default='default.jpg',upload_to='profile_pic')
    #profile_pic will the folder where all the profile pics will be uploaded

    def __str__(self):#This determines how we want it to be displayed,when we query the profile
        return f'{self.user.username} Profile'
        #so it will print the username of the profile and 'Profile' as it is

    #incase user uploads big images or wallpaper we want to resize it so,we override the save method
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)#to run the default save()
        img=Image.open(self.image.path)
        #if the image exceeds 600 px we want it to be resized to 600 px
        if img.height>600 or img.width>600:
            new_size=(600,600)
            img.thumbnail(new_size)
            img.save(self.image.path)