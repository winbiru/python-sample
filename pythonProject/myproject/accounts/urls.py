from django.urls import path

from .views import SignUpView

app_name = 'accounts'

urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    # url(r'^signup/$', SignUpView.as_view(), name='signup'),
    # path('', views.home, name="home"),
    # path('login/', views.login_user, name='login'),
    # path('logout/', views.logout_user, name='logout'),
    # path('register/', views.register_user, name='register'),
    # path('edit_profile/', views.edit_profile, name='edit_profile'),
    # path('change_password', views.change_password, name='change_password'),
]
