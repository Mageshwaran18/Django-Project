from itertools import product
from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth import authenticate , login
from .models import Account_Details, Product


def home(request):
    return render(request,'home.html')

def SignUp(request):
    if request.method=='POST':
        email=request.POST.get('email')
        firstname=request.POST.get('firstname')
        lastname=request.POST.get('lastname')
        contact=request.POST.get('contact')
        password=request.POST.get('password')
        address=request.POST.get('address')
        account_details=Account_Details(first_name=firstname,last_name=lastname,Email=email,Contact_no=contact,Address=address,Password=password)
        account_details.save()
        messages.success(request,"Account Created Successfully")
        return redirect(SignUpSuccess)
    
    return render(request,'sign_up.html')
# Create your views here.

def Login(request):
    if request.method == 'POST':
        email = request.POST.get('Email')
        password = request.POST.get('password')

        try:
            account = Account_Details.objects.get(Email=email)
        except Account_Details.DoesNotExist:
            account = None
        
        if account is not None and account.Password == password:
            shopping = Product.objects.all()
            return render(request, 'shop.html',{'shopping':shopping})
        else:
            return render(request, 'sign_in_unsuccess.html')
    else:
        return render(request, 'login.html')
    
def SignUpSuccess(request):
    return render(request,'sign_up_success.html')

def SignInSuccess(request):
    return render(request,'sign_in_success.html')

def SignUnSuccess(request):
    return render(request,'sign_in_unsuccess.html')

def shop(request):
    shopping = Product.objects.all()
    return render(request, 'shop.html', {'shopping': shopping})