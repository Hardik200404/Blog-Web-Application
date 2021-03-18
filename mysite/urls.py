"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from .import view
from django.contrib.auth import views as auth_views
#auth_views is a functionality which django provides us for login and logout ops
#these imports below are to serve static content on to our django app,i.e., profile pics
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('Blog.urls')),
    path('home/',view.home,name='Home'),
    path('login/',auth_views.LoginView.as_view(template_name='users_template/login.html'),name='Login'),
    path('logout/',auth_views.LogoutView.as_view(template_name='users_template/logout.html'),name='Logout'),
    path('password-reset/',auth_views.PasswordResetView.as_view(template_name='users_template/password_reset.html'),name='Password_reset'),
    path('password-reset/done/',auth_views.PasswordResetDoneView.as_view(template_name='users_template/password_reset_done.html'),name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(template_name='users_template/password_reset_confirm.html'),name='password_reset_confirm'),
    path('password-reset-complete/',auth_views.PasswordResetCompleteView.as_view(template_name='users_template/password_reset_complete.html'),name='password_reset_complete'),
]#auth_views has class based functionality ,hence we also include '.as_view', so that django treats its as view page
#rather than redering template in the class itself we defined template_name inside as_view function

if settings.DEBUG:#to ensure that the profile can only be fetched when the debug is true
    urlpatterns+= static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
#since we are in devlopment mode,serving static content from media_root is ok,but its not recommended for production