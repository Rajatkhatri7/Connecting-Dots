from urllib import response
import uuid
from django.shortcuts import render
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib import messages

from PIL import Image



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

def imgtopdf(request):
    if request.method == 'POST':
        try: 

            uploaded_file = request.FILES["imagefile"]
            filename = uploaded_file.name

            tmp_path = f'/tmp/{filename}'
            with open(tmp_path, 'wb') as destination:
                destination.write(uploaded_file.read())

            pdf_path = f'/tmp/{filename.split(".")[0]}.pdf'
            image = Image.open(tmp_path)
            im = image.convert('RGB')
            im.save(pdf_path)

            fs = FileSystemStorage(pdf_path)
            resp = FileResponse(fs.open(pdf_path), content_type='application/pdf')
            resp['content-Disposition'] = f'attachment; filename="{uuid.uuid4().hex}.pdf"'


            return render(request , 'fileconversion/imgtopdf.html', {"imgname":filename,'resp': resp})
        except:
            messages.add_message(request, messages.ERROR, "No image selected or uploaded")
            
            return render(request, "fileconversion/imgtopdf.html")
        
    else:
        return render(request, "fileconversion/imgtopdf.html")

def imgcompression(request):
    return render(request, 'fileconversion/imgcompression.html')


def mergepdf(request):
    return render(request, 'fileconversion/mergepdf.html')

