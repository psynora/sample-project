
from django.contrib import admin
from django.urls import path

from loapp import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('nupp/', views.index),
]
