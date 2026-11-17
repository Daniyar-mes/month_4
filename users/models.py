from django.db import models
from django.contrib.auth.models import User

class CustomUser(User):
    photo = models.ImageField(upload_to='users/')
    phone_number = models.CharField(max_length=13)
    GENDER = (
        ('MALE', 'MALE'),
        ('FAMALE', 'FAMALE')
    )

    date_bird = models.DateField()
    gender = models.CharField(max_length=10, choices=GENDER)
    city = models.CharField(max_length=25)
