from django.shortcuts import render

# Create your views here.

def fileconversion(request):
    return render(request, 'fileconversion/fileconversion.html')

def pdftoimg(request):
    return render(request, 'fileconversion/pdftoimg.html')

def imgtopdf(request):
    return render(request, 'fileconversion/imgtopdf.html')


def imgcompression(request):
    return render(request, 'fileconversion/imgcompression.html')


def mergepdf(request):
    return render(request, 'fileconversion/mergepdf.html')

