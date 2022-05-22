# -*- coding: utf-8 -*-
from django import forms

class PdfUploadForm(forms.Form):
    pdf_file = forms.FileField(
        label='Select a pdf file',
    )

class ImgUploadForm(forms.Form):
    image_file = forms.FileField(
        label='Select a image file',
    )