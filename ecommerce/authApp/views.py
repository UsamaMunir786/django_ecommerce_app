from django.shortcuts import render,redirect, HttpResponse

# Create your views here.

def signup(request):
	
	if request.method == 'POST':
		email = request.POST['email']
		password = request.POST['pass1']
		confirm_password = request.POST['pass2']

		if password != confirm_password:
			return HttpResponse('password incorrect')

		try:
			if User.objects.get(username = email):
				return HttpResponse('email already exist')
		except Exception as e:
			pass

		user = User.objects.create_user(email,email,password)
		user.save()
		return HttpResponse('user created', email)

	return render(request, 'signup.html')
		


def handlelogin(request):
	return render(request, 'authentication/handlelogin.html')

def handlelogout(request):
	return redirect('/auth/login')