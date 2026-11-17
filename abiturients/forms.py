from django import forms
from abiturients.models import Abiturients

class AbiturientsForm(forms.ModelForm):
    class Meta:
        model = Abiturients
        fields = '__all__'
