from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import registrationform,UserUpdateForm,ProfileUpdate

#function for registration
def register(req):
    if req.method=='POST':
        form=registrationform(req.POST)#creating a instance of reg from which we modified in our forms.py
        if form.is_valid():#to validate the posted data,to ensure all the fields were filled properly
            form.save()#to save the user data
            #lets get the username
            username=form.cleaned_data.get('username')
            messages.success(req,f'Account created for {username}')
            return redirect('Login')
    else:#if its a get req
        form=registrationform()#creating a instance of reg from which we modified in our forms.py
    
    context={'form':form}
    return render(req,'users_template/register.html',context)#sending form instance to the register html file


#login_required is a decorator,it ensures that this func can only be used when a user is logged in
@login_required
def profile(req):
    if req.method=='POST':#this will run when will acutally update the data
        #creating instances of the form classes and will pass to our template
        user_form=UserUpdateForm(req.POST,instance=req.user)
        profile_form=ProfileUpdate(req.POST,req.FILES,instance=req.user.profile)
        #defining instances lets django fill the update fields with the initial data

        #to validate the data we receive from the form
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()

            #once saved
            messages.success(req,'Profile updated!!')
            return redirect('profile')
    else:
        user_form=UserUpdateForm(instance=req.user)
        profile_form=ProfileUpdate(instance=req.user.profile)
        #instances are defined so that the username and email field are pre filled with the current details
    context={
        'user_form':user_form,
        'profile_form':profile_form
    }
    return render(req,'users_template/profile.html',context)

