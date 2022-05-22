import os

from django.db import models
from django.conf import settings

from PyPDF2 import PdfFileReader
from wand.image import Image

from fileconversion.extra import ContentTypeRestrictedFileField
from pdf2image import convert_from_path
import time


def make_upload_path(instance, filename):
    """Generates upload path for FileField"""
    return settings.PDF_OUTPUT_FILES_URL + "/%s" % (filename)


class PdfFile(models.Model):
    pdf_file = ContentTypeRestrictedFileField(
        upload_to=make_upload_path,
        content_types=['application/pdf'],
        max_upload_size=5242880
    )

    def convert_to_png(self, width=0, height=0):
        self.__convert_to_img__(width, height, 'png')

    def convert_to_jpg(self, width=0, height=0):
        self.__convert_to_img__(width, height, 'jpg')

    def __convert_to_img__(self, width, height, format='jpg'):
        size = ''
        if width and height:
            size = '_' + str(width) + 'x' + str(height) + 'px'

        filename = self.pdf_file.name
        filepath  = os.path.join(settings.MEDIA_ROOT, filename)
      
        
        i = 1
        pages_name = []

        pages = convert_from_path(filepath, 200)
        for p in pages :
            p.save( "Page_" + str(i) + '.' + format,'JPEG')
            pages_name.append("Page_" + str(i) + '.' + format)
            i+=1    

        
        # os.rmdir(filepath)
                # img.save(filename = output_dir + str(i) + '.' + format)

        #remove pages from rootdir