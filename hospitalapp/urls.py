
from django.contrib import admin
from django.urls import path
from hospitalapp import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index),
    path('inner/', views.inner),
    path('about/', views.about),
    path('doctors/', views.doctor),
    path('appointment/', views.appointment),
]
