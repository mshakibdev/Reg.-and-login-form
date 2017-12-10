from django.shortcuts import render
from django.http import HttpResponse
from .models import MyUser,UserProfile
def get_info(request):
	if request.method == 'POST':
		username = request.POST.get('your_name')
		passwords = request.POST.get('password')
		try:
			obj, created = MyUser.objects.get_or_create(your_name=username,password =passwords)
			if created==True :
				return HttpResponse('<h1>Registration Completed</h1>')
			else:
				return HttpResponse('<h1>Username is already exist</h1>')
		except:
			  	return HttpResponse('<h1>Invalid Password</h1>')
	return render(request, 'user.html')
	
def login(request):
	if request.method == 'POST':
		username = request.POST.get('your_name')
		passwords = request.POST.get('password')
		
		try:
			a = MyUser.objects.filter(your_name=username,password =passwords)
			if a:
				return HttpResponse('<h1>Login Succesfull ! ;)</h1>')
			else:
				return HttpResponse("<h1>Username or password incorrect</h1>")
		except:
			return HttpResponse("<h1>Invalid Password</h1>")
	return render(request, 'login.html')

def profile(request):
	if request.method == 'POST':
		get_name_request = request.POST.get('name')
		

		if request:
			try:
				get_user_name = UserProfile.objects.get(user__your_name=get_name_request)
				#y1= y.objects.values('email')
				user = UserProfile.objects.get(name=get_user_name )	
				#a= y[0]['name']						
				context = {'users':user}
				return render(request,'profile.html',context)
			except:	
				return HttpResponse("<h1>User Doesn't exist</h1>")
	return render(request,'profile.html')
		
