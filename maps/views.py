from django.shortcuts import render
from django.contrib.auth import(
 authenticate,
 get_user_model,
 login,
 logout,



	)
from .form import *
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect


# Create your views here.
def map_view(request):
	return render(request,'mapiing.html',{})

def mapp_view(request):
	return render(request,'mapp.html',{})

def login_view(request):
	title = "Login"
	form = UserLoginForm(request.POST or None)
	if form.is_valid():
		username = form.cleaned_data.get("username")
		password =  form.cleaned_data.get("password")

	return render(request,"form.html",{"form":form , "title":title})

def register_view(request):
	title = "Register"
	if request.method == 'POST':
		form = UserRegistrationForm(request.POST or None)
		if form.is_valid():
			userObj = form.cleaned_data
			print(userObj)
			username = userObj['username']
			email =  userObj['email']
			password =  userObj['password']
			if not (User.objects.filter(username=username).exists() or User.objects.filter(email=email).exists()):
				User.objects.create_user(username, email, password)
				user = authenticate(username = username, password = password)
				login(request, user)
				return HttpResponseRedirect('/')
			else:
				raise forms.ValidationError('Looks like a username with that email or password already exists')
	else:
		form = UserRegistrationForm()
	return render(request,"register.html",{"form":form,"title":title})

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})

def logout_view(request):
	return render(request,"form.html",{})

def form_submission_view(request):
	print("The form is submitted.")
	username = request.POST("username")
	email = request.POST("email")
	password = request.POST("password")
def donation_view(request):
	
	form = donationForm(request.POST or None)
	if form.is_valid():
			
		name = form.cleaned_data.get('name')
		amount = form.cleaned_data.get('amount')

	return render(request, 'donation.html',{'form':form})
def EventsView(request):
	return render(request, 'events.html')

def IndexView(request):
	return render(request, 'index.html')