from django.shortcuts import render, HttpResponse, redirect

def index(request):
	return render(request, "survey_form/index.html")
def process(request):
	if request.method == "POST":
		request.session['name'] = request.POST['name']
		request.session['location'] = request.POST['location']
		request.session['language'] = request.POST['language']
		if 'count' not in request.session:
			request.session['count'] = 0
		else:
			request.session['count'] += 1
		return redirect('/survey_form/result')
	else:
		return redirect('/survey_form')
def result(request):
	return render(request, "survey_form/result.html")