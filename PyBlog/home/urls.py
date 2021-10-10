from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from home import views
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static
from home import views as user_views

urlpatterns = [
    path('',views.home, name= 'home'),
    path('register/',user_views.register, name= 'register'),
    path('about',views.about, name= 'about'),
    path('contact',views.contact, name= 'contact'),
    path('profile/',user_views.profile, name= 'profile'),
    path('login/', auth_views.LoginView.as_view(template_name='home/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='home/logout.html'), name='logout'),   

] 

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


