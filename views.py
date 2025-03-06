from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages  # Importing the messages module
from django.contrib. auth.models import User
# Create your views here.

@login_required(login_url="login")
def products(request):
    return render(request, 'products.html')


def loginpage(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('products')  # Assuming products is a valid URL name
        else:
            messages.error(request, 'Invalid username or password')  # Add error message if auth fails
    return render(request, 'loginpage.html')

def dashboard_page(request):
    return render(request, 'dashboard.html')

def header_page(request):
    return render(request, 'header.html')

def footer_page(request):
    return render(request, 'footer.html')

def products_page(request):
    return render(request, 'products.html')

@login_required(login_url="loginpage")
def signup(request):
    return render(request, "loginpage")

def signup_page(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']
        
        if password != password2:  # Check if passwords match
            messages.error(request, 'Passwords do not match')
            return redirect('signup_page')  # Redirect back to signup if passwords don't match

        try:
            user = User.objects.create_user(first_name=first_name, last_name=last_name, username=username, email=email, password=password)
            user.save()
            messages.success(request, 'Account created successfully! Please log in.')
            return redirect('loginpage')  # Redirect to login page after successful signup
        except Exception as e:
            messages.error(request, str(e))  # In case there's an error while creating the user
    
    return render(request, 'signuppage.html')

def orders_page(request):
    return render(request, 'orders.html')

def users_page(request):
    return render(request, 'users.html')

def checkout_page(request):
    return render(request, 'checkout.html')

def ordersucess_page(request):
    return render(request, 'ordersucess.html')


def base_page(request):
    return render(request, 'base.html')

def logout_view(request):
    logout(request)
    messages.success(request, 'Successfully logged out')
    return redirect('loginpage')  # Redirect to the login page

def deals_view(request):
    return render(request, 'deals.html')

def home_view(request):
    return render(request, 'home.html')
