from django.shortcuts import render , redirect

import base64
import pytesseract
from django.contrib import messages
from PIL import Image
import cv2
import numpy as np

from .algorithms.scoring import scoring_algorithm
from .algorithms.frequency import frequency_algorithm


def aiservices(request):
    return render(request, 'aiservices/aiservices.html')

import requests
from bs4 import BeautifulSoup


def summarization(request):
    req_url = request.POST.get('url')
    long_text = request.POST.get('long-text')
    sentence_no = request.POST.get('number')
    
    algorithm = request.POST.get('algorithm')
    result_list = []

    if req_url:

        page = requests.get(req_url)

        soup = BeautifulSoup(page.content, 'html.parser')
        soup_tag = list(filter(lambda p: len(list(p.children)) < 2, soup.find_all(['p', 'div'], class_=None, id=None)))
        text = ' '.join(map(lambda p: p.text, soup_tag))
        if text == '':
            text = 'No Paragraphs Found!'
        original_text = text.replace('\xa0', ' ')
    


    else:
        original_text = long_text

    if algorithm == '1':
        result_list = scoring_algorithm.scoring_main(long_text, int(sentence_no))
    elif algorithm == '2':
        result_list = frequency_algorithm.frequency_main(long_text, int(sentence_no))

    summary = ' '.join(result_list)
    

    context = {'data': summary, 'original_text': original_text}


    return render(request, 'aiservices/summerization_home.html',context)


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
            return render(request, "aiservices/extraction.html")
        lang = request.POST["language"]

        pil_img = Image.open(image)

        img = np.array(pil_img , dtype = np.uint8)
        img_gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)


        # img_gray  = cv2.imread(img, cv2.IMREAD_GRAYSCALE)

        #adaptive thresholding
        # thresh = cv2.adaptiveThreshold(img_gray, 250, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 11, 11)

        # adaptive thresholding
        # cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2)

        # img = Image.open(image)
        text = pytesseract.image_to_string(img_gray, lang=lang)
        # return text to html
        return render(request, 'aiservices/extraction.html', {"ocr": text, "image": image_base64})

    return render(request, 'aiservices/extraction.html')


