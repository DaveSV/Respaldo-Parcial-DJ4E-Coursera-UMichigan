#from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def myview(request):
    n_visits = request.session.get('n_visits', 0) + 1
    request.session['n_visits'] = n_visits
    message = "Hello my friend"
    if n_visits > 4: del(request.session['n_visits'])
    resp = HttpResponse(message)
    # resp = render(request, 'hello/hello.html', {'message':message})
    resp.set_cookie('dj4e_cookie', '63868568', max_age=1000)
    return resp
