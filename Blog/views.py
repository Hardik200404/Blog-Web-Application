from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.models import User
from .models import Post
#Post class in models.py is the table which holds the data
#importing class based views below
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
#as we are using class based views we cannot use decorators,e.g @loginrequired
#the above import helps us to go to class only if user is logged in,in our case createpost
#userpasses... means that only the user who is logged in can make changes to their own posts
'''def home(req):
    #Post.objects.all() returns everything and context is sent as parameter to the home.html with all db data
    context={
        'posts':Post.objects.all()
    }
    return render(req,'blog_templates/home.html',context)'''

class PostListView(ListView):
    model=Post
    #when the url hits here this class will look for a template
    #<app>/<model>_<viewtype>.html,i.e blog,Post,listview,so we need to mention how to use the existing template
    template_name='blog_templates/home.html'
    context_object_name='posts'
    ordering=['-Date_posted']#this ensures the newest posts to displayed at the top
    paginate_by=3#to show 3 post per page

class UserPostListView(ListView):#to show the posts of a particular user
    model=Post
    template_name='blog_templates/user_posts.html'
    context_object_name='posts'
    paginate_by=3#to show 3 post per page
    def get_queryset(self):
        user=get_object_or_404(User,username=self.kwargs.get('username'))
        #if the user exists we get the username in user
        #to filter only those post whose author is the user clicked
        return Post.objects.filter(Author=user).order_by('-Date_posted')

class PostDetailView(DetailView):
    model=Post
    #this view is used when the user wants to check a particular post
    template_name='blog_templates/post_detail.html'

class PostCreateView(LoginRequiredMixin,CreateView):#for user to create post
    model=Post
    fields=['Title','Content']#providing these fields to be filled in
    template_name='blog_templates/post_new.html'

    #to set the author for the posted data,we override the form_valid method
    def form_valid(self,form):
        form.instance.Author=self.request.user
        return super().form_valid(form)
        #this super func is running our form_valide on our parent class

class PostUpdateView(LoginRequiredMixin,UserPassesTestMixin,UpdateView):#for user to update post
    model=Post
    fields=['Title','Content']#providing these fields to be filled in
    template_name='blog_templates/post_new.html'

    #to set the author for the posted data,we override the form_valid method
    def form_valid(self,form):
        form.instance.Author=self.request.user
        return super().form_valid(form)
    def test_func(self):#this func will check if the logged in user matches the author of post
        #to get the current post
        post=self.get_object()
        if self.request.user==post.Author:
            return True
        return False

class PostDeleteView(LoginRequiredMixin,UserPassesTestMixin,DeleteView):#to delete a post
    model=Post
    template_name='blog_templates/post_delete.html'
    success_url="/"#to be redirected to home page when a post is deleted
    def test_func(self):#this func will check if the logged in user matches the author of post
        #to get the current post
        post=self.get_object()
        if self.request.user==post.Author:
            return True
        return False

def about(req):
    return render(req,'blog_templates/about.html')