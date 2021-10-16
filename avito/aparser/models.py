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
    #description = models.TextField("Описание")
    #url = models.SlugField(max_length=160, unique=True)
    parentId = models.PositiveSmallIntegerField()
    #parentIdKey = models.ForeignKey(Category, verbose_name="Фильм", on_delete=models.CASCADE)
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"