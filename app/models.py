from django.db import models

class Todo(models.Model):
    STATUS=(
        ('bajarildi','Bajarildi'),
        ('bajarilmadi','Bajarilmadi'),
        ('bajarilmoqda','Bajarilmoqda')
    )
    title=models.CharField(max_length=150)
    time=models.DateTimeField()
    docs=models.CharField(max_length=150)
    status=models.CharField(max_length=30,choices=STATUS)
