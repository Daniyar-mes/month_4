from django import forms
from django.contrib.auth.forms import UserCreationForm
from users.models import CustomUser

GENDER = (
    ('MALE', 'MALE'),
    ('FAMALE', 'FAMALE')
)

class CustomRegisterForm(UserCreationForm):
    photo = forms.ImageField(required=True)
    email = forms.EmailField(required=True, initial='@gmail.com')
    phone_number = forms.DateField(required=True, initial='996')
    date_bir = forms.DateField(required=True)
    gender = forms.ChoiceField(choices=GENDER, required=True, initial='Male')
    city = forms.CharField(max_length=25, initial='Bishkek')


    class Meta:
        model = CustomUser
        fields = (
            'username',
            'first_name',
            'password',
            'password2',
            'photo', 
            'email',
            'phone_number',
            'date_bir',
            'gender',
            'city'
        )
        def save(self, commit=True):
            user = super(CustomRegisterForm, self).save(commit=False)
            user.email = self.cleaned_data['email']
            if commit:
                user.save()
                return user