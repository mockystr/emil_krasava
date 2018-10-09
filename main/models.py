from django.db import models
from django.urls import reverse, reverse_lazy


class Category(models.Model):
    name = models.CharField(max_length=200, db_index=True, verbose_name="Наименование")
    slug = models.SlugField(max_length=200, db_index=True, unique=True)

    class Meta:
        ordering = ('name',)
        verbose_name = "Категория"
        verbose_name_plural = "Категории"

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("main:product_list_by_category", args=[self.slug])


class Item(models.Model):
    name = models.CharField(max_length=200, verbose_name="Наименование")
    slug = models.SlugField(max_length=200, unique=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Цена товара")
    description = models.TextField(blank=True, verbose_name="Описание")
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name="Категория")
    available = models.BooleanField(default=True, verbose_name="Доступно")
    image_main = models.ImageField(upload_to="items/%Y/%m/%d", verbose_name="Главная фотография")

    class Meta:
        ordering = ('name',)
        verbose_name = "Предмет"
        verbose_name_plural = "Предметы"

    def __str__(self):
        return "{}".format(self.name)

    def get_absolute_url(self):
        return reverse('main:product_detail', args=[self.id, self.slug])


class Image(models.Model):
    img = models.ImageField(upload_to="items/%Y/%m/%d", verbose_name="Дополнительная фотография")
    item = models.ForeignKey(Item, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Фотография"
        verbose_name_plural = "Фотографии для предметов"

    def __str__(self):
        return "Фотография для {}".format(self.item.name)
