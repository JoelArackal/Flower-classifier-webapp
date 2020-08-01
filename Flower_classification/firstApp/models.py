from django.db import models

# Create your models here.

class Flowers(models.Model):
    flower_image = models.ImageField(upload_to ='flower_images')
    id = models.AutoField(primary_key=True)

    def __str__(self):
        return str(self.id)