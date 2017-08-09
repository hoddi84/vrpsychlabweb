from django.conf.urls import url
from main import views

# Template tagging
app_name = 'main'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^other/$', views.other, name='other'),
    url(r'^testing/$', views.testing, name='testing'),
    url(r'^postview/$', views.postview, name='postview'),
    url(r'^fileview/$', views.fileview, name='fileview'),
]
