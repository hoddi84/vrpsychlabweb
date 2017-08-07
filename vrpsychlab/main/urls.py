from django.conf.urls import url
from main import views

# Template tagging
app_name = 'main'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^other/$', views.other, name='other'),
]
