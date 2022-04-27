from django.urls import path
from . import views





urlpatterns = [

    
    path('fileconverison', views.fileconversion, name='fileconversion'),
    path('fileconversion/pdftoimg', views.pdftoimg, name='pdftoimg'),
    path('fileconversion/imgtopdf', views.imgtopdf, name='imgtopdf'),
    path('fileconversion/imgcompression', views.imgcompression, name='imgcompression'),
    path('fileconversion/mergepdf', views.mergepdf, name='mergepdf'),


]