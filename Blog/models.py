from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

class Post(models.Model):
    #defining fields in our table
    Title=models.CharField(max_length=100)
    Content=models.TextField()
    Date_posted=models.DateTimeField(default=timezone.now)
    Author=models.ForeignKey(User,on_delete=models.CASCADE)
    #on_delete=models.cascade, ensures that if the user is deleted the post is gone too
    #but this a one way street , if we delete a post the user won't get deleted, that would be bad

    def __str__(self):#when queried it would only return only title
        return self.Title

    def get_absolute_url(self):
        #this is to get the pk of newly created post and pass it to reverse,to get the url
        #once we get the url,views.py will handle the redirect when a post is created
        return reverse('post-detail',kwargs={'pk':self.pk})