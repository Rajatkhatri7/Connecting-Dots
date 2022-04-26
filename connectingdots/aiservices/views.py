from django.shortcuts import render , redirect

import base64
import pytesseract
from django.contrib import messages
from PIL import Image

# Create your views here.


def aiservices(request):
    return render(request, 'aiservices/aiservices.html')


def summarization(request):
    return render(request, 'aiservices/summarization.html')


def extraction(request):


    if request.method == "POST":
        try:
            image = request.FILES["imagefile"]
            # encode image to base64 string
            image_base64 = base64.b64encode(image.read()).decode("utf-8")
        except:
            messages.add_message(
                request, messages.ERROR, "No image selected or uploaded"
            )
            return render(request, "home.html")
        lang = request.POST["language"]
        img = Image.open(image)
        text = pytesseract.image_to_string(img, lang=lang)
        # return text to html
        return render(request, 'aiservices/extraction.html', {"ocr": text, "image": image_base64})

    return render(request, 'aiservices/extraction.html')


