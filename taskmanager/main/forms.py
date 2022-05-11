from .models import task
from django.forms import ModelForm, TextInput, Textarea


class taskForm(ModelForm):
    class Meta:
        model = task
        fields = ["title", "task" ]
        widgets = {
            "title": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите Название'
            }),
            "task": Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Введите Описание'
            }),
        }
