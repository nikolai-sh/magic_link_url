from . import views
from django.urls import path


urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('send-magic-link/', views.send_magic_link, name='send-magic-link'),
    path('login/token/', views.login_with_magic_link),

]