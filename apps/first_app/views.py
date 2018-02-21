from django.shortcuts import render, HttpResponse, redirect
  # the index function is called when root is visited
def index(request):
	response = "Placeholder to later display all the list of blogs"
	return HttpResponse(response)
def new(request):
	response = "Placeholder to display a new form to create a new blog"
	return HttpResponse(response)
def create(request):
	return redirect('/')
def show(request, number):
	return HttpResponse("Placeholder to display blog " + number)
def edit(request, number):
	return HttpResponse("Placeholder to edit blog " + number)
def delete(request, number):
	return redirect('/')


