from django.urls import path
from .import views
from .views import PostListView,PostDetailView,PostCreateView,PostUpdateView,PostDeleteView,UserPostListView
from users import views as users_views#if the register button is pressed it would open /register

#we we mention a class in the url route , we need to add as_view()
urlpatterns = [
    path('',PostListView.as_view() ,name ='blog-home'),
    path('user/<str:username>',UserPostListView.as_view() ,name ='user-posts'),
    path('post/<int:pk>/',PostDetailView.as_view() ,name ='post-detail'),
    #url for particular post depending upon the primary key of the post
    path('post/new/',PostCreateView.as_view() ,name ='post-create'),
    path('post/<int:pk>/update/',PostUpdateView.as_view() ,name ='post-update'),
    path('post/<int:pk>/delete/',PostDeleteView.as_view() ,name ='post-delete'),
    path('about/',views.about,name='blog-about'),
    path('register/',users_views.register,name="register"),
    path('profile/',users_views.profile,name="profile"),
]#giving a name to the path keeps things simple,and we use these names in our links to refer them
