from django.db import models

# Create your models here.



class Sittenge_data(models.Model):
    access_token = models.CharField(max_length=300)
    STORE_ID = models.CharField(max_length=300)

    def __str__(self):
        return self.access_token