from django.shortcuts import render, HttpResponse, redirect

def index(request):
	return render(request, "session_words/index.html")
def process(request):
	if request.method == "POST":
		if 'word' not in request.session:
			element_list = [request.POST['word'],request.POST['color']]
			request.session['word'] = element_list

			
			return redirect('/session_words')
		else:
			element_list = [request.POST['word'],request.POST['color']]
			word_list = request.session['word'] 
			word_list.append(element_list)
			request.session['word'] = word_list
			
			return redirect('/session_words')
	else:
		return redirect('/session_words')
def clear(request):
	if 'word' not in request.session:
		return redirect('/session_words')
	else:
		del request.session['word']
		return redirect('/session_words')
