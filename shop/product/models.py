from django.db import models, transaction

from . import tasks

class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.FloatField()
    image = models.ImageField(upload_to='images/products/original')
    thumbnail = models.ImageField(upload_to='images/products/thumbnail', null=True)

    def save(self, *args, **kwargs):
        created = self.pk is None
        with transaction.atomic():
            if created:
                transaction.on_commit(
                    lambda: tasks.create_product_thumbnail.delay(self.pk)
                )
            super().save(*args, **kwargs)