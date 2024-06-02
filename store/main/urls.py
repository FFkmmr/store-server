from django.urls import path
from . import views
from django.contrib import admin

urlpatterns = [
    path('admin/', admin.site.urls, name='admin_panel'),
    path('', views.index, name='home'),
    path('about', views.about, name='about'),
]
 