from django.http import HttpResponse
from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout

from .forms import SignUpForm, SigninForm

# Create your views here.
def error_404(request, exception):
    return render(request, 'account/404.html')

def signin(request):
    form = SigninForm()
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password1')
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request, user)
                return redirect('domregis:register_dom')
            else:
                message = 'Your account is inactive. Please try again'
                return HttpResponse(message)
        else:
            print("Someone tried to login and failed.")
            print("They used username: {} and password: {}".format(username,password))
            messages.error(request, 'Invalid login details given, please input the correct credential')
            #return render(request, 'account/page-login.html', {'message':"Invalid login details given",'form': form})
            return redirect('account:signin')
    return render(request, 'account/page-login.html', {'form': form})

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            #login(request,user)
            return redirect('account:signin') 
        
    else:
        form = SignUpForm()
    #context = 
    return render(request, 'account/page-signup.html', {'form':form})

def signout(request):
    logout(request)
    return redirect('account:signin')