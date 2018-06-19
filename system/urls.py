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
    url(r'^$', views.system_page, name = "system_page"),
    url(r'^add/$', views.add_system, name = "add_system"),
    url(r'^edit/([A-z-]+)/$', views.edit_system, name = "edit_system"),
    url(r'^crud/$', views.crud_system, name = "crud_system"),
    url(r'^get_system/$', views.get_system, name = "get_system"),
    url(r'^get_system_count/$', views.get_system_count, name = "get_system_count"),
    url(r'^host/$', views.host_page, name = "host_page"),
]
