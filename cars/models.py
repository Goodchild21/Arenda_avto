from django.db import models
from PIL import Image


class Categories(models.Model):
    name = models.CharField(max_length=150, unique=True, verbose_name='Название')
    slug = models.SlugField(max_length=200, unique=True, blank=True, null=True, verbose_name='URL')

    class Meta:
        db_table = 'category'
        verbose_name = 'Категорию'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name


class Products(models.Model):
    name = models.CharField(max_length=150, unique=True, verbose_name='Название')
    slug = models.SlugField(max_length=200, unique=True, blank=True, null=True, verbose_name='URL')
    description = models.TextField(blank=True, null=True, verbose_name='Описание')
    image = models.ImageField(upload_to='cars_pics', blank=True, null=True, verbose_name='Изображение')
    price = models.DecimalField(default=0.00, max_digits=7, decimal_places=2, verbose_name='Цена')
    # discount = models.DecimalField(default=0.00, max_digits=7, decimal_places=2, verbose_name='Скидка в %')
    # quantity = models.PositiveIntegerField(default=0, verbose_name='Количество')
    category = models.ForeignKey(to=Categories, on_delete=models.CASCADE, verbose_name='Категория')

    class Meta:
        db_table = 'product'
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'
        ordering = ('id',)

    # def __str__(self):
    #     return f'{self.name} Количество - {self.quantity}'

    def display_id(self):
        return f'21.11.2024.{self.id:03}'

    # def rendering(self):
    #     # super(Profile, self).save(*args, **kwargs)
    #
    #     img = Image.open(self.image.path)
    #     if img.height > 100 or img.width > 100:
    #         output_size = (100, 100)
    #         img.thumbnail(output_size)
    #         img.save(self.image.path)

    # def sell_price(self):
    #     if self.discount:
    #         return round(self.price - self.price*self.discount/100, 2)
    #
    #     return self.price