from django.db import models

class Todo(models.Model):
    STATUS=(
        ('bajarildi','Bajarildi'),
        ('bajarilmadi','Bajarilmadi'),
        ('bajarilmoqda','Bajarilmoqda')
    )
    title=models.CharField(max_length=150)
    time=models.TimeField()
    docs=models.DateTimeField()
    status=models.CharField(max_length=30,choices=STATUS)
