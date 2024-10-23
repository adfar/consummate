from django.db import models

class Food(models.Model):
    upc = models.CharField(max_length=4)

    def __str__(self):
        return self.upc

class Expiration(models.Model):
    upc = models.ForeignKey(Food, on_delete=models.CASCADE)
    expiration_date = models.DateField()