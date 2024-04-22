from django.shortcuts import redirect, render,HttpResponse
from home.models import Contact,Sale
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth import login as login_user
from django.contrib.auth import logout as logout_user
from django.contrib.auth.decorators import login_required

@login_required(login_url='login')
# Create your views here.

def index(request):
    return render(request,'index.html')
    #return HttpResponse("This is about page")

def about(request):
    return render(request,'about.html')
    #return HttpResponse("This is about page")

def contact(request):
    if request.method == 'POST':
        name=request.POST.get('name')
        email=request.POST.get('email')
        phone=request.POST.get('phone')
        desc=request.POST.get('desc')
        contact=Contact(name=name,email=email,phone=phone,desc=desc)
        contact.save()
        messages.success(request, "Submited!")

    return render(request,'contact.html')
    #return HttpResponse("This is service page")

def nearby(request):
    return render(request,'nearby.html')

def dealer(request):
    return render(request,'dealer.html')

def advice(request):
    return render(request,'advice.html')


def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        pass1= request.POST.get('pass')
        
        
        user = authenticate(request, username=username, password=pass1)
        print(user)
        
        if user is not None:
            
            login_user(request, user)
            return redirect('home')  
        else:
            return HttpResponse('Wrong username or password')  
    
    return render(request, 'login.html')
    

def signup(request):
    if request.method=='POST':
        uname=request.POST.get('username')
        email=request.POST.get('email')
        pass1=request.POST.get('password1')
        pass2=request.POST.get('password2')
        if pass1!=pass2:
            messages.error(request,"Passwords do not match")
            return redirect('signup')
        else:
            my_user=User.objects.create_user(uname,email,pass1)
            my_user.save()
            return redirect('login')
    return render(request,'signup.html')

def landing(request):
    return render(request,'landing.html')

def logout(request):
    logout_user(request)
    return redirect('login')

def sale(request):
   if request.method == 'POST':
        product_name = request.POST.get('ProductName', '')  # Ensure the correct form field name is used
        product_desc=request.POST.get('ProductPrice','')
        product_price=request.POST.get('ProductDescription','')
        sale_item=Sale(ProductName=product_name,ProductDescription=product_desc,ProductPrice=product_price)
        sale_item.save()
        messages.success(request, "Submited!")
   return render(request, 'sale.html')


