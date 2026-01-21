from django.shortcuts import render
from .models import Post
from django.http import HttpResponse


def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'blog/home.html', context)


def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})


def setsession(request):
    request.session['fav_color'] = 'blue'
    return HttpResponse("Session set: fav_color = blue")    
def getsession(request):
    fav_color = request.session.get('fav_color', 'red')
    return HttpResponse(f"Favorite color is {fav_color}")

def delsession(request):
    try:
        del request.session['fav_color']
    except KeyError:
        pass
    return HttpResponse("Session key 'fav_color' deleted")
def clearsession(request):

    request.session.flush()
    return HttpResponse("All session data cleared")
def visitcount(request):
    visit_count = request.session.get('visit_count', 0)
    visit_count += 1
    request.session['visit_count'] = visit_count
    return HttpResponse(f"Visit count: {visit_count}")
def setexpiry(request):
    request.session.set_expiry(10)  # Session expires in 10 seconds
    return HttpResponse("Session expiry set to 10 seconds")
def checkexpiry(request):
    expiry_age = request.session.get_expiry_age()
    return HttpResponse(f"Session will expire in {expiry_age} seconds")
def clearsessionexpiry(request):
    request.session.set_expiry(0)  # Session expires on browser close
    return HttpResponse("Session expiry cleared; will expire on browser close")

def customexpiry(request):
    request.session.set_expiry(300)  # Session expires in 5 minutes
    return HttpResponse("Session expiry set to 5 minutes")
def checkcustomexpiry(request):
    expiry_age = request.session.get_expiry_age()
    return HttpResponse(f"Custom session will expire in {expiry_age} seconds")
def deletecustomexpiry(request):
    request.session.set_expiry(0)  # Session expires on browser close
    return HttpResponse("Custom session expiry deleted; will expire on browser close")
def incrementcounter(request):
    counter = request.session.get('counter', 0)
    counter += 1
    request.session['counter'] = counter
    return HttpResponse(f"Counter incremented to {counter}")
def resetcounter(request):
    request.session['counter'] = 0
    return HttpResponse("Counter reset to 0")
def getcounter(request):
    counter = request.session.get('counter', 0)
    return HttpResponse(f"Current counter value is {counter}")
def deletecounter(request):
    try:
        del request.session['counter']
    except KeyError:
        pass
    return HttpResponse("Counter deleted from session")
def setmultiplekeys(request):
    request.session['key1'] = 'value1'
    request.session['key2'] = 'value2'
    return HttpResponse("Multiple session keys set: key1 and key2")
def getmultiplekeys(request):
    key1 = request.session.get('key1', 'not set')
    key2 = request.session.get('key2', 'not set')
    return HttpResponse(f"key1: {key1}, key2: {key2}")
def deletemultiplekeys(request):
    try:
        del request.session['key1']
        del request.session['key2']
    except KeyError:
        pass
    return HttpResponse("Multiple session keys deleted: key1 and key2") 
