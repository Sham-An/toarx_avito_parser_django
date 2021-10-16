from django.db import models

from .constants import STATUS_NEW, STATUS_READY


class Task(models.Model):
    title = models.TextField(
        verbose_name='Название задания',
        unique=True,
    )
    url = models.URLField(
        verbose_name='Ссылка на раздел',
        unique=True,
    )
    status = models.IntegerField(
        verbose_name='Статус задания',
        choices=(
            (STATUS_NEW, 'Новое'),
            (STATUS_READY, 'Готово'),
        ),
        default=STATUS_NEW,
    )

    def __str__(self):
        return f'#{self.pk} {self.title}'

    class Meta:
        verbose_name = 'Задание'
        verbose_name_plural = 'Задания'


class Product(models.Model):
    task = models.ForeignKey(
        to=Task,
        verbose_name='Задание',
        null=True,
        blank=True,
        on_delete=models.PROTECT,
    )
    title = models.TextField(
        verbose_name='Заголовок',
    )
    price = models.PositiveIntegerField(
        verbose_name='Цена',
    )
    currency = models.TextField(
        verbose_name='Валюта',
        null=True,
        blank=True,
    )
    url = models.URLField(
        verbose_name='Ссылка на объявление',
        unique=True,
    )
    published_date = models.DateTimeField(
        verbose_name='Дата публикации',
    )

    def __str__(self):
        return f'#{self.pk} {self.title}'

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'

class Category(models.Model):
    """Категории"""
    name = models.CharField("Категория", max_length=150)
    name_en_dir = models.CharField("КатегорияEN", max_length=150,
    null=True, blank=True,)
    #description = models.TextField("Описание")
    #url = models.SlugField(max_length=160, unique=True)
    parentId = models.PositiveSmallIntegerField()
    #JsId = models.PositiveSmallIntegerField()
    JsId = models.PositiveSmallIntegerField(
        verbose_name='JsonKey',
        null=True,
        blank=True,
    )
    #parentIdKey = models.ForeignKey(Category, verbose_name="Фильм", on_delete=models.CASCADE)
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"

class Region(models.Model):
    """Регионы"""
    name = models.CharField("Регион", max_length=150)
    name_en_dir = models.CharField("КатегорияEN", max_length=150,
    null=True, blank=True,)
    #description = models.TextField("Описание")
    #url = models.SlugField(max_length=160, unique=True)
    JsId = models.PositiveSmallIntegerField(
        verbose_name='JsonKey',
        null=True,
        blank=True,
    )
    #parentIdKey = models.ForeignKey(Category, verbose_name="Фильм", on_delete=models.CASCADE)
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Регион"
        verbose_name_plural = "Регионы"

class City(models.Model):
    """Населенные пункты"""
    name = models.CharField("Населенные пункты", max_length=150)
    name_en_dir = models.CharField("Населенные пунктыEN", max_length=150,
    null=True, blank=True,)
    #description = models.TextField("Описание")
    #url = models.SlugField(max_length=160, unique=True)
    JsId = models.PositiveSmallIntegerField(
        verbose_name='JsonKey',
        null=True,
        blank=True,
    )
    parent_Id = models.ForeignKey(Region, verbose_name="Регион", on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Населенный пункт"
        verbose_name_plural = "Населенные пункты"
