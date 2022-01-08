from django.db import models

# Create your models here.
class Image(models.Model):
    date=models.DateField(auto_now_add=True)
    photo=models.ImageField(upload_to='myimage')

    
