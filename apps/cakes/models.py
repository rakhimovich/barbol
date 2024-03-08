import os
from django.db import models
from utils.image_path import upload_cakes

class Cake(models.Model):
    title = models.CharField(
        max_length=59,
        verbose_name='Название',
    )
    description = models.TextField(
        verbose_name='Описание'
    )
    price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        verbose_name='Цена',
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Дата создания'
    )
    image = models.ImageField(
        upload_to=upload_cakes,
        verbose_name='Картинка',
    )
    
    def delete(self, using=None, keep_parents=False):
        os.remove(self.image.path)
        super().delete(using=None, keep_parents=False)

    def __str__(self):
        return self.title