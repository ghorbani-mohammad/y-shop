from PIL import Image
from io import BytesIO
from celery import shared_task
from django.core.files.base import File

from . import models

@shared_task()
def create_product_thumbnail(product_id):
    product = models.Product.objects.get(pk=product_id)
    image = Image.open(product.image.path)
    new_width, new_height = (160, 160)
    image.thumbnail((new_width, new_height))
    img_temp = BytesIO()
    image.save(img_temp, "PNG")
    product.thumbnail = File(img_temp, product.image.name.split("/")[-1])
    product.save()