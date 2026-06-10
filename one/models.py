from django.db import models

# Create your models here.

class Hotel(models.Model):
    name=models.CharField(max_length=30)
    place=models.CharField(max_length=30)

    def __str__(self):
        return self.name

class Food(models.Model):
    name=models.CharField(max_length=30)
    price=models.IntegerField()
    hotel=models.ForeignKey(Hotel,on_delete=models.CASCADE,related_name='htl')

    def __str__(self):
        return self.name
    



     