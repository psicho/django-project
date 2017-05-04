"""homese URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from mainapp.views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', main),
    url(r'^main/$', main, name='main'),
    url(r'^catalog/$', catalog, name='catalog'),
    url(r'^product/$', product, name='product'),
    url(r'^delivery/$', delivery, name='delivery'),
    url(r'^contacts/$', contacts, name='contacts'),
    url(r'^pay/$', pay, name='pay'),
]

urlpatterns += [
    url(r'^user/login/', login),
    url(r'^user/logout/', logout),
    url(r'^user/registration/$', registration, name='registration'),
]