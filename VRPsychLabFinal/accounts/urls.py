from django.conf.urls import url
from django.contrib.auth import views as auth_views
from . import views

app_name = "accounts"

urlpatterns = [
    url(regex=r'^login/$', view=auth_views.LoginView.as_view(template_name="accounts/login.html"), name='login'),
    url(regex=r'^logout/$', view=auth_views.LogoutView.as_view(), name='logout'),
]
