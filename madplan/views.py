from django.shortcuts import render

def index(request):
	number = 6
	name = "Asshole"
	return render(request, 'index.html',{
					'number': number,
					'name': name,
					})

def about(request):
	return render(request, 'about.html')

def contact(request):
	return render(request, 'contact.html')