from django.shortcuts import render , redirect

import base64
import pytesseract
from django.contrib import messages
from PIL import Image

# Create your views here.


from .algorithms.scoring import scoring_algorithm
from .algorithms.frequency import extraction, frequency_algorithm


def aiservices(request):
    return render(request, 'aiservices/aiservices.html')


def summarization(request):
    url = request.GET.get('url')
    long_text = request.GET.get('long-text')
    # sentence_no = int(request.GET.get('number'))
    sentence_no = 7
    algorithm = request.GET.get('algorithm')
    result_list = []

    if url:
        long_text = extraction.extract(url)  # text extraction using BS
        original_text = url
    else:
        original_text = long_text

    if algorithm == '1':
        result_list = scoring_algorithm.scoring_main(long_text, sentence_no)
    elif algorithm == '2':
        result_list = frequency_algorithm.frequency_main(long_text, sentence_no)

    summary = ' '.join(result_list)

    context = {'data': summary, 'original_text': original_text}


    return render(request, 'aiservices/summarization.html',context)


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


