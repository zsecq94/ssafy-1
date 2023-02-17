from django import forms
from .models import Movie
from django.forms.widgets import NumberInput


class MovieForm(forms.ModelForm):
    genres = [
        ('코미디', '코미디'),
        ('공포', '공포'),
        ('로맨스', '로맨스'),
    ]
    genre = forms.ChoiceField(choices=genres)
    score = forms.CharField(label='Score', widget=forms.TextInput(attrs={'min':0,'max': '5','type': 'number', 'step': 0.5}))    
    release_date = forms.DateTimeField(widget=NumberInput(attrs={'type': 'date'}), label="날짜")

    class Meta:
        model = Movie
        fields = '__all__'