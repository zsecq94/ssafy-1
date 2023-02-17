from django import forms
from .models import Travel

class TravelForm(forms.ModelForm):
    location = forms.CharField(
        label='Location',
        widget=forms.TextInput(
            attrs={
                'placeholder': 'ex) 제주도',
                'maxlength': 10,
            }
        )
    )

    plan = forms.CharField(
        label='Plan',
        widget=forms.Textarea(
            attrs={
                'placeholder': 'ex) 슉.슈슉.',
                'rows': 5,
                'cols': 50,
            }
        )
    )

    start_data = forms.DateTimeField(
        widget=forms.TextInput(
            attrs={
                'placeholder': 'ex) 2022-02-22'
            }
        )
    )
    end_data = forms.DateTimeField(
        widget=forms.TextInput(
            attrs={
                'placeholder': 'ex) 2022-02-22'
            }
        )
    )

    class Meta:
        model = Travel
        fields = '__all__'