from django.shortcuts import render, HttpResponse,redirect
from django.contrib.auth.models import User 
from django.contrib.auth import authenticate,login,logout
# from django.contrib.auth.decorators import login_required

# @login_required(login_url='login1')

def LoginPage(request):

    if request.method == "POST":
        uname = request.POST.get('username')
        pass1 = request.POST.get('password')
        user = authenticate(request,username=uname, password=pass1)
        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            return HttpResponse("username and password is incorrect!!!")

    return render(request,'login.html')   

def SignUpPage(request):
    error_messages = {'username_exists': '', 'password_mismatch': ''}

    if request.method == 'POST':
        uname = request.POST.get('username')
        email = request.POST.get('email')
        pass1 = request.POST.get('password')
        pass2 = request.POST.get('confirmPassword')

        # Check if passwords match
        if pass1 != pass2:
            error_messages['password_mismatch'] = "Password does not match"
        else:
            # Check if the username already exists
            if User.objects.filter(username=uname).exists():
                error_messages['username_exists'] = "Username already exists. Please choose a different one."
            else:
                # Create a new user
                my_user = User.objects.create_user(username=uname, email=email, password=pass1)
                my_user.save()

                return redirect('login1')

    return render(request, 'signup.html', {'error_messages': error_messages})

def HomePage(request):
    return render(request,'home.html')

def LogoutPage(request):
    logout(request)
    return redirect('login1')
