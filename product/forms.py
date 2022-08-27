from django.forms import ModelForm
from .models import *




class AddCategory(ModelForm):
    class Meta:
        model = Category
        fields = ['title', 'description', 'is_active', 'image']
