from django.urls import path
from . import views




urlpatterns = [

    
    path('aiservices', views.aiservices, name='aiservices'),
    path('aiservices/summarization', views.summarization, name='summarization'),
    path('aiservices/extraction', views.extraction, name='extraction'),


]