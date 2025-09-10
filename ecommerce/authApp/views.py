from django.shortcuts import render,redirect

# Create your views here.

def signup(request):
	return render(request, 'authentication/signUp.html')

def handlelogin(request):
	return render(request, 'authentication/handlelogin.html')

def handlelogout(request):
	return redirect('/auth/login')