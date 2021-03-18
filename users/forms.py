#we created this file to add additional fields to our form,i.e email address and profile picture
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile
class registrationform(UserCreationForm):
    email=forms.EmailField()#default is 'required=True'
    #meta class ensures that any user which will be added,will be updated to the User model,with given fields
    class Meta:
        model=User
        fields=[
            'username',
            'email',
            'password1',
            'password2',
        ]
#pass2 is confirmation password

#creating a profile form for the user,when they need to update their profile
class UserUpdateForm(forms.ModelForm):#by inheriting modelform we are letting djnago know this form is to update a model  
    email=forms.EmailField()
    class Meta:
        model=User
        fields=['username','email']

#to update profile pic we need the profile model so its imported at the top
class ProfileUpdate(forms.ModelForm):
    class Meta:
        model=Profile
        fields=['image']