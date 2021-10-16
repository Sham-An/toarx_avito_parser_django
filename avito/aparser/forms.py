from django import forms

from .models import Task
from .models import Product
from .models import Category
from .models import Region
from .models import City


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = (
            'title',
            'url',
            'status',
        )
        widgets = {
            'title': forms.TextInput,
        }


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = (
            'title',
            'price',
            'currency',
            'url',
            'published_date',
        )
        widgets = {
            'title': forms.TextInput,
            'currency': forms.TextInput,
        }


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = (
            'name',
            'parentId',
            'JsId'
        )
        widgets = {
            'name': forms.TextInput,
        }


class RegionForm(forms.ModelForm):
    class Meta:
        model = Region
        fields = ('name', 'JsId')

        widgets = {
            'name': forms.TextInput,
        }

class CityForm(forms.ModelForm):
    class Meta:
        model = City
        fields = (
            'name',
            'parent_Id',
            'JsId'
        )
        widgets = {
            'name': forms.TextInput,
        }
