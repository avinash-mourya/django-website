from django.shortcuts import render
from .forms import *
from .models import *
from django.http import *
def index(request):
    return render(request,'myapp/index.html')
# def user1(request):
#     if request.method == "POST":
#       form = user_form(request.POST)
#       if form.is_valid():
#             form.save()
#             return HttpResponseRedirect('/userform/')    
#     else:
#       form = user_form()   
    # return render(request,'myapp/form.html')  
def asd(request):
    return render(request,"myapp/form1.html") 
# def user2(request):
#     firstname = request.POST['firstname']
#     lastname = request.POST['lastname']
#     email = request.POST['email']
#     address = request.POST['address']
#     phone = request.POST['phone']
#     password = request.POST['password']
#     sv = users(first_name=firstname,last_name=lastname,email=email,password=password,address=address,phone_no=phone)
#     sv.save()
#     return render(request,"myapp/form1.html")
def login(request):
    return render(request,"myapp/login.html") 
def login_page(request):
    email = request.POST['email']
    password = request.POST['password']
    user = users2.objects.get(email=email)
    if user.email in email and user.password in password:
      return render(request,"myapp/user.html",{'name':user.first_name+" "+user.last_name}) 
    else:
          return render(request,"myapp/login.html",{'error':'you have enter wrong email and password'})


def camera(request):
    return render(request,"camera.html")