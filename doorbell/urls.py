"""doorbell URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from .views import *
from . import views
from django.conf.urls.static import static
from django.conf import settings
urlpatterns = [
    path('admin/', admin.site.urls),
    # path('test/', views.Test, name='test'),
    path('', views.Index, name='index'),
    path('register', views.Register, name='register'),
    path('login', views.Login, name='login'),
    path('logout/',views.Logout, name='logout'),
    path('dashboard/', views.Dashboard ,name='dashboard'),
    path('about', About, name='about'),
    path('contact', Contact, name='contact'),               
    path('add-property', Add_property, name='add-property'),
    path('more-property', Search_eng, name='more_property'),
    path('products/<int:product_id>/', views.product_detail, name='product_detail'),
    path('book_property/<int:property_id>/', views.Add_booking, name='book_property'),
    path('verify-otp/', verify_otp_view, name='verify_otp'),
    path('delete_user/<int:user_id>/', views.delete_user, name='delete_user'),
   

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)