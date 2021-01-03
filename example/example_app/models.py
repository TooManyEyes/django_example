from django.db import models


# Create your models here.
class MyData(models.Model):
    name = models.CharField(max_length=20, help_text="Название")
    data = models.CharField(max_length=1000000, help_text="Данные")

    def __str__(self):
        return self.name
