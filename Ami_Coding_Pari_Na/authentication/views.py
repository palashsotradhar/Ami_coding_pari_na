from django.shortcuts import render,HttpResponse,redirect
from django.views import View
from .forms import loginform,regiform
from django.contrib.auth import authenticate,logout,login as auth_login
from django.contrib.auth.models import User



def Login(request):
    if not request.user.is_authenticated:
        fr = loginform()
        if request.method == 'POST':
            fr = loginform(data = request.POST)
            if fr.is_valid():
                umail = fr.cleaned_data['username']
                upass = fr.cleaned_data['password']
                user = authenticate(username = umail,password = upass)
                if user is not None:
                    auth_login(request,user)

                    return redirect('khoj')
                else:
                    return redirect('regi/')
        return render(request,'authentication/login.html',{'fr':fr})
    else:return HttpResponse('You already logged in')


def user_logout(request):
    logout(request)
    return redirect('login')

# i Used Class based view for my own comfort
class Regi(View):
    def get(self,request):
        fr = regiform()
        return render(request, 'authentication/registration.html',{'fr':fr})
    def post(self,request):
        fr = regiform(request.POST)
        if fr.is_valid():
            email = fr.cleaned_data['email']
            username = fr.cleaned_data['username']

            password = fr.cleaned_data['password']
            repassword = fr.cleaned_data['repassword']
            # i am not using error handling here.I using simple python technique to check password and repassword
            if password != repassword:
                return HttpResponse('Refresh This page your password and repassword is not same')


            myuser = User.objects.create_user(username = username,email = email,password = password)

            myuser.save()
            fr.save()


            return redirect('login')


