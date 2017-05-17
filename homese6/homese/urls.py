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
    # url(r'^admin/$', admin_page, name='admin_page'),
    url(r'^admin007/$', admin_page, name='admin_page'),
    url(r'^admin007/delete/user/(\d+)$', delete_user),
    url(r'^admin007/get_user_form/(\d+)$', get_user_form),
    url(r'^admin007/create/user/(\d*)$', create_user),
]

urlpatterns += [
    url(r'admin007/jewels/', admin_jewels, name='admin_jewels'),
    url(r'^admin007/create/jewels/$', admin_jewels_create, name='jewels_create'),
    url(r'^admin007/delete/jewels/(\d+)$', admin_jewels_delete, name='jewels_delete'),
    url(r'^admin007/update/jewels/(\d+)$', admin_jewels_update, name='jewels_update'),
    url(r'^admin007/detail/jewels/(\d+)$', admin_jewels_detail, name='jewels_detail')
]

urlpatterns += [
    url(r'^jewels/$', jeweler, name='jeweler'),
    url(r'^jewels/(\d+)/$', jeweler, name='jeweler'),
    url(r'^catalog/$', jeweler, name='jeweler'),
]

if settings.DEBUG:
    # static files (images, css, javascript, etc.)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)