from django.urls import re_path, path
from . import views


urlpatterns = [
    re_path('^fileupload/', views.FileFieldView.as_view()),
    re_path(r'^new/$', views.festival_new, name='festival_new'),
    re_path(r'^(?P<region>\w+)/$', views.festival_list, name='festival_list'),
    re_path(r'^(?P<region>\w+)/(?P<pk>\d+)/$', views.festival_detail, name='festival_detail'),
    re_path(r'^complete', views.festival_complete, name='festival_complete'),
]