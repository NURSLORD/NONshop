from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.contrib.auth.models import User


# Create your views here.
def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        password2 = request.POST["password2"]
        if password != password2:
            messages.error(request, 'Passwords are not correct!')
            return redirect('register')
        user = User()
        user.username = username
        user.set_password(password)
        user.save()
        messages.success(request, 'you are in site')
        return redirect('test')
    return render(request, "user/register.html")


def login_own(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'You are logined!')
            return redirect('test')
        else:
            messages.success(request, 'You are not logined!')
            return redirect('my_login')

    return render(request, 'user/login.html')


def logout(request):
    return redirect('logout_my')


#
#
# def comment_test(request):
#     return render(request, 'user/comment.html')
#
#
# def logout(request):
#     return redirect('logout')

def test_auth(request):
    return render(request, 'user/test_auth.html')
