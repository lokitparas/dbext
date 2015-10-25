from django.shortcuts import render

def signin(request):
	return render(request,'main.html')

def signup(request):
	return render(request,'signup.html')
# Create your views here.
