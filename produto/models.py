from collections.abc import Iterable
from django.db import models
from PIL import Image
import os
from django.conf import settings

class Product(models.Model):
    class Meta:
        verbose_name = 'produto'
        verbose_name_plural = 'produtos'
    
    name = models.CharField(max_length=50)
    short_description = models.TextField(max_length=125)
    long_description = models.TextField(max_length=255)
    image = models.ImageField(upload_to='%Y/%m')
    slug = models.SlugField(unique=True)
    price_marketing = models.FloatField()
    price_marketing_promotional = models.FloatField(default=0)
    types = models.CharField(
        default='v',
        max_length=1,
        choices=(
            ('v','variaçao'),
            ('s', 'simples'),
        )
    )
    @staticmethod
    def resize_image(img,new_width=800):
        img_full_path = os.path.join(settings.MEDIA_ROOT,img.name)
        image_pil = Image.open(img_full_path)
        original_heigth, original_width = image_pil.size
        
        if original_width <= new_width:
            image_pil.close()
            return
        new_heigth = round((new_width * original_heigth) / original_width)
        new_image = image_pil.resize((new_heigth, new_width), Image.LANCZOS)
        new_image.save(
            img_full_path,
            optimize=True,
            quality=50
        )

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        max_image_size = 800

        if self.image:
            self.resize_image(self.image,max_image_size)


    def __str__(self):
        return self.name
    
class Variation(models.Model):
    class Meta:
        verbose_name = 'variacao'
        verbose_name_plural = 'variaçoes'
    
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    name = models.CharField(max_length=125)
    price = models.FloatField()
    price_promotional = models.FloatField(default=0)
    stock = models.PositiveIntegerField(default=1)

    def __str__(self):
        return self.name