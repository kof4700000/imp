"""wh4imp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
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
from . import views

urlpatterns = [
    #url(r'^sign_in/$', views.sign_in_page, name = "sign_in"),
    url(r'^sign_up/$', views.sign_up_page, name = "sign_up"),
    url(r'^current_user/$', views.current_user, name = "current_user"),
    url(r'^login/$', views.login, name = "login"),
    url(r'^logout/$', views.logout, name = "logout"),
    url(r'^crud_user/$', views.crud_user, name = "crud_user"),
    url(r'^init_address/$', views.init_adderss, name = "init_address"),
    url(r'^get_detail/([A-z]*)/$', views.get_detail, name = 'get_detail'),
    url(r'^edit_user/([A-z]*)/$', views.edit_user, name = "edit_user"),
]
