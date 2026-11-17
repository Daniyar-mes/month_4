from django.db import models

class Abiturients(models.Model):
    full_name = models.CharField('ФИО', max_length=150)
    photo = models.ImageField('загрузите фото', upload_to='abiturients/')
    FACULTAT = (
        ('IT', 'IT'),
        ('МЕНЕДЖМЕНТ', 'МЕНЕДЖМЕНТ'),
        ('БИЗНЕС', 'БИЗНЕС')
    )
    document_ort = models.FileField('загрузите ОРТ', upload_to='abiturients_doc/')
    facultat = models.CharField('Выберите факультет', max_length=100, choices=FACULTAT)
    created_at = models.DateTimeField(auto_now_add=True)
