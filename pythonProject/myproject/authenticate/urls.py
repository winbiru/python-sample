from django.conf.urls import url
from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
app_name='authenticate'
urlpatterns = [
    path('', views.register),
    path('register/', views.register, name="register"),
    path('login/', auth_views.LoginView.as_view(template_name="authenticate/login.html"), name="login"),
    path('logout/', auth_views.LogoutView.as_view(next_page='/'), name='logout'),
]