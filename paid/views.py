from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib.auth import authenticate
from .models import UserResult
# Create your views here.
def home(request):
    return render(request,"base.html",{'pagename': 'base'})

def signin(request):
    if request.method=="POST":
        username=request.POST["username"]
        password=request.POST["password"]
        obj = authenticate(username=username,password=password)
        print(obj)
        if obj is not None:
            user_login = auth.login(request,obj)
            return redirect('/calculator')
    return render(request,"signin.html",{'pagename':'signin'})

def signup(request):
    if request.method=="POST":
        first_name=request.POST["first_name"]
        email = request.POST["email"]
        username=request.POST["username"]
        password=request.POST["password"] 
        obj = User.objects.create_user(first_name=first_name,email=email,username=username,password=password)
        return redirect('/signin')
    return render(request,"signup.html",{'pagename':'signup'})

def calculator(request):
    result = 0
    if request.method=="POST":
        num1 = request.POST["num1"]
        num2 = request.POST["num2"]
        operator = request.POST["operator"]
        result = eval(num1+operator+num2)
        obj = UserResult.objects.create(num1 = num1, num2=num2,result=result,operator=operator,user=request.user)
    user_results = UserResult.objects.filter(user=request.user)
    return render(request,'calculator.html',{'pagename':'calculator','result':result,'ur':user_results})

def logout(request):
    auth.logout(request)
    return redirect('/')