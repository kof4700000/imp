from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.DocListView.as_view(), name = "doc_page"),
    url(r'^detail/(?P<pk>[0-9]+)/$', views.DocDetailView.as_view(), name = "doc_detail"),
    url(r'^upload/$', views.upload_file, name = "upload_file"),
]
