from django.urls import path
from . import views 

urlpatterns = [
    path('emails/', views.envia_email, name='enviaemail.urls'),
]