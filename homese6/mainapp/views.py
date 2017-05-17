from django.contrib import auth
from django.shortcuts import render, HttpResponseRedirect, get_object_or_404
from django.http import Http404, JsonResponse
from mainapp.forms import MyRegistrationForm, MyCorrectionForm, UserChangeForm, JewelForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import user_passes_test
from django.template.context_processors import csrf
from django.template import loader
from mainapp.models import Jewel, Category
# from mainapp.models import Teach, Work, Hobby

def main(request):
    return render(request, "index.html")

def catalog(request):
    jewels = Jewel.objects.all()
    categories = Category.objects.all()
    return render(request, "catalog.html", {'categories': categories, 'jewels': jewels})

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

@user_passes_test(lambda u: u.is_superuser)  # доступ у админке только суперпользователю
def admin_page(request):
    # TODO: сделать доступ к админке только суперпользователю
    users = User.objects.all()
    #user_form = MyRegistrationForm()
    user_form = MyCorrectionForm()
    return render(request, 'admin_page.html', {'users': users, 'form': user_form})

def delete_user(request, user_id):
    user = get_object_or_404(User, id=user_id)
    user.delete()
    return HttpResponseRedirect('/admin007/')

def create_user(request, user_id=None):
    """
    Создает Пользователя(User)
    Или редактирует существующего, если указан  user_id
    """
    if request.is_ajax():
        print('user_id = ', user_id)
        if not user_id:
            print('Not user_id')
            user = UserChangeForm(request.POST)
        else:
            user = get_object_or_404(User, id=user_id)
            user = UserChangeForm(request.POST or None, instance=user)
        if user.is_valid():
            user.save()
            users = User.objects.all()
            html = loader.render_to_string('inc-users_list.html', {'users': users}, request=request)
            data = {'errors': False, 'html': html}
            return JsonResponse(data)
        else:
            errors = user.errors.as_json()
            return JsonResponse({'errors': errors})
    raise Http404

def get_user_form(request, user_id):
    """
    Возвращает заполненную форму для редактирования Пользователя(User) с заданным user_id
    """
    if request.is_ajax():
        user = get_object_or_404(User, id=user_id)
        user_form = MyCorrectionForm(instance=user)
        context = {'form': user_form, 'id': user_id}
        context.update(csrf(request))
        html = loader.render_to_string('inc-correction_form.html', context)
        data = {'errors': False, 'html': html}
        return JsonResponse(data)
    raise Http404

def jeweler(request, category_id):
    jewels = Jewel.objects.filter(category__id=category_id)
    categories = Category.objects.all()
    return render(request, 'jewel_page.html', {'categories': categories, 'jewels': jewels})

def admin_jewels(request):
    jewels = Jewel.objects.all()
    return render(request, 'admin_jewels.html', {'jewels': jewels})

def admin_jewels_create(request):
    if request.method == 'POST':
        form = JewelForm(request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/admin007/jewels/')
        else:
            return render(request, 'admin_jewels_create.html', {'form': form})
    return render(request, 'admin_jewels_create.html', {'form': JewelForm()})

def admin_jewels_delete(request, id):
    jewels = get_object_or_404(Jewel, id=id)
    jewels.delete()
    return HttpResponseRedirect('/admin007/jewels/')

def admin_jewels_update(request, id):
    jewels = get_object_or_404(Jewel, id=id)
    if request.method == 'POST':
        # form = GemsForm(request.POST or None, instance=gem)
        form = JewelForm(request.POST, instance=jewels)
        if form.is_valid():
            jewels.save()
            return HttpResponseRedirect('/admin007/jewels/')
        else:
            return render(request, 'admin_jewels_update.html', {'form': form})
    return render(request, 'admin_jewels_update.html', {'form': JewelForm(instance=jewels)})
def admin_jewels_detail(request, id):
    jewels = get_object_or_404(Jewel, id=id)
    return render(request, 'admin_jewels_detail.html', {'jewels':jewels})
