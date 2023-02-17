from django import forms
from .models import Article

# Create your models here.
class ArticleForm(forms.ModelForm):
    title = forms.CharField(
        label = '제목',
        widget=forms.TextInput(
            attrs={
                'PlaceHolder': '제목을 입력하세요...',
                'maxlenth': 20,
            }
        )
    )

    content = forms.CharField(
        label = '내용',
        widget=forms.Textarea(
            attrs={
                'PlaceHolder': '내용을 입력하세요...',
                'rows': 5,
                'clos': 50,
            }
        )
    )

    class Meta:
        model = Article
        fields = '__all__'