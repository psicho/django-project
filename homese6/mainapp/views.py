from django.contrib import auth
from django.shortcuts import render, render_to_response, HttpResponseRedirect
from django.http import Http404
from mainapp.forms import MyRegistrationForm
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

def registration_low(request):
    if request.method == 'POST':
        errors = {}  # Тут будем хранить ошибки, чтобы отобразить на странице
        username = request.POST.get('name')
        email = request.POST.get('email')
        email2 = request.POST.get('confirm_email')
        password = request.POST.get('password')
        password2 = request.POST.get('confirm_password')
        print(request.POST)
        # Validate data
        if email != email2:
            errors['email'] = 'does not match'
        if password != password2:
            errors['password'] = 'does not match'
        user = User(username=username, email=email)
        # Пароли хранятся в виде хэшей, поэтому их нельзя передавать напрямую
        user.set_password(password)
        # Проверяем, существует ли пользователь с таким именем
        try:
            user.validate_unique()
        except ValidationError as er:
            errors.update(er.message_dict)
        # Если есть ошибки, передаем их в контексте шаблону, который умеет их отображать
        if errors:
            return render(request, 'registration_low.html', {'reg_errors': errors})
        # Если ошибок нет, сохраняем пользователя в базе, перенаправляем на главную
        user.save()
        return HttpResponseRedirect("/")
    return render(request, 'registration_low.html')

def registration(request):
    if request.method == 'POST':
        form = MyRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
        context = {'form': form}
        return render(request, 'registration.html', context)
    context = {'form': MyRegistrationForm()}
    return render(request, 'registration.html', context)
