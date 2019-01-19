from django.urls import re_path
from django.conf.urls import url
from . import views

urlpatterns = [
    re_path(r'^all/$', views.showall),
    re_path(r'^get/(?P<video_id>\d+)/$', views.showone),
    re_path(r'^addcomment/(?P<video_id>\d+)/$', views.addcom),
    re_path(r'^addlike/ajax/$', views.addlike),
    url(r'^$', views.home, name='home'),
]