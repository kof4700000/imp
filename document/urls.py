from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.doc_page, name = "doc_page"),
    url(r'^detail/([0-9]*)/$', views.doc_detail, name = "doc_detail"),
    url(r'^upload/$', views.upload_file, name = "upload_file"),
]
