from django.shortcuts import render, HttpResponse, redirect
from django.utils.crypto import get_random_string
def index(request):
	if 'count' not in request.session:
		request.session['count'] = 0
	else:
		request.session['count'] += 1
	return render(request, "random_word/index.html")
def count(request):
	if request.method == "POST":
		request.session['word'] = get_random_string(length=14)
		return redirect('/random_word')
	else:
		return redirect('/random_word')