from django import forms
from .models import Memo

class MemoForm(forms.ModelForm):
    summary = forms.CharField(
        label='Summary',
        widget=forms.TextInput(
            attrs={
                'class': 'my-summary',
                'placeholder': 'summary',
                'maxlength': 20,
            }
        )
    )

    memo = forms.CharField(
        label='Memo',
        widget=forms.Textarea(
            attrs={
                'class': 'my-memo',
                'placeholder': 'memo',
                'rows': 5,
                'cols': 50,
            }
        ),
        # error_messages={
        #     'required': '내용 입력하라고..',
        # }
    )

    class Meta:
        model = Memo
        fields = '__all__'