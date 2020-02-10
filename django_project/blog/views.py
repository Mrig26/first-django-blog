from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

posts=[
	{
	'author':'Joe Noe',
	'title':'Blog Post 1',
	'content':'Content 1',
	'date':'August 27 1219'
	},
	{
	'author':'Sarah',
	'title':'Blog Post 2',
	'content':'Content 2',
	'date':'April 19 2020'
	}
]

def home(request):
	context={
	'posts':posts
	}
	return render(request, 'blog/home.html', context)

def about(request):
	return render(request, 'blog/about.html')
