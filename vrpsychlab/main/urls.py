from django.conf.urls import url
from main import views

# Template tagging
app_name = 'main'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^postview/$', views.liveView, name='live_procedure'),
    url(r'^convert/$', views.convertView, name='convert_file'),
    url(r'^vogabyggd/$', views.vogabyggdView, name='vogabyggd'),
]
