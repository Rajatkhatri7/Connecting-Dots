import imp
from urllib import response
import uuid
from django.shortcuts import render
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib import messages
from django.conf import settings

from django.http import FileResponse


from PIL import Image
from django.core.files.storage import FileSystemStorage


import base64
import os

from .forms import PdfUploadForm
from .models import PdfFile
# Create your views here.

def fileconversion(request):
    return render(request, 'fileconversion/fileconversion.html')

def pdftoimg(request):

    if request.method == 'POST':
        form = PdfUploadForm(request.POST, request.FILES)
        if form.is_valid():
            new_pdf = PdfFile(pdf_file = request.FILES['pdf_file'])
            new_pdf.save()

            # convert to jpg file after uploading
            # if you don't pass parameters then the images
            # will have the actual size
            new_pdf.convert_to_jpg()

            

    else:
        form = PdfUploadForm()

    pdf_files = PdfFile.objects.all()

    

    return render(request,
        'fileconversion/pdftoimage.html',
        {'pdf_files': pdf_files, 'form': form}
    )


import time

def imgtopdf(request):
        if request.method == "POST":
            try:
                image = request.FILES["imagefile"]
                   # encode image to base64 string
                image_base64 = base64.b64encode(image.read()).decode("utf-8")
            except:
                messages.add_message(
                request, messages.ERROR, "No image selected or uploaded"
                )
                return render(request, "fileconversion/imgtopdf.html")

            pil_img = Image.open(image)
            tmp_path = os.path.join(settings.MEDIA_ROOT)

            pdf_path = 'tmp.pdf'
            im = pil_img.convert('RGB')
            im.save(pdf_path)

            fs = FileSystemStorage(pdf_path)
            resp = FileResponse(fs.open(tmp_path), content_type='application/pdf')
            resp['content-Disposition'] = f'attachment; filename="{pdf_path}"'

            time.sleep(5)

            return resp


        
        else:
          return render(request, "fileconversion/imgtopdf.html")

def imgcompression(request):
    return render(request, 'fileconversion/imgcompression.html')


def mergepdf(request):
    return render(request, 'fileconversion/mergepdf.html')

