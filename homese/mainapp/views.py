from django.contrib import auth
from django.shortcuts import render, render_to_response, HttpResponseRedirect
from django.http import Http404
# from mainapp.models import Teach, Work, Hobby

def main(request):
    return render(request, "index.html")

def catalog(request):
    return render(request, "catalog.html")

def product(request):
    return render(request, "product.html")

def contacts(request):
    return render(request, "contacts.html")

def delivery(request):
    return render(request, "delivery.html")

def pay(request):
    return render(request, "pay.html")

def login(request):
    if request.method == 'POST':
        username = request.POST['login']
        password = request.POST.get('password')
        user = auth.authenticate(username=username, password=password)
        if user:
            auth.login(request,user)
            return HttpResponseRedirect('/')
        else:
            return render(request, 'index.html', {'username':username, 'errors':True})
    else:
        raise Http404


def logout(request):
    auth.logout(request)
    return HttpResponseRedirect('/')