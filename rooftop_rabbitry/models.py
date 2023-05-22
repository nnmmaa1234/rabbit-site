from django.db import models
from PIL import Image

# Create your models here.
class RabbitBreed(models.Model):
    breed_name = models.CharField(max_length=50)
    description = models.TextField(default='')

    def __str__(self):
        return self.breed_name


class Rabbit(models.Model):

    status = [
        ('Available', 'Available'),
        ('Sold', 'Sold'),
        ('Reserved', 'Reserved'),
    ]

    breed   = models.ForeignKey(RabbitBreed, on_delete=models.CASCADE)
    name    = models.CharField(max_length=50)
    age     = models.IntegerField()
    weight  = models.IntegerField()
    color   = models.CharField(max_length=50)
    price   = models.IntegerField()
    status  = models.CharField(max_length=50, choices=status, default='Available')
    image  = models.ImageField(
        upload_to='E:/One Drive/OneDrive/Python Projects/potfolio_projs/Rabbitry/RooftopRabbitry/rooftop_rabbitry/static/images', 
        default ='E:/One Drive/OneDrive/Python Projects/potfolio_projs/Rabbitry/RooftopRabbitry/rooftop_rabbitry/static/images/default.jpg'
        )

    # def save(self, *args, **kwargs):
    #     super().save(*args, **kwargs)
    #     img = images.open(self.image.path)
    #     width, height = img.size
    #     if width != height:
    #         min_dim = min(width, height)
    #         x1 = (width - min_dim) // 2
    #         y1 = (height - min_dim) // 2
    #         x2 = x1 + min_dim
    #         y2 = y1 + min_dim
    #         img = img.crop((x1, y1, x2, y2))
    #         img.save(self.image.path)

    def __str__(self):
        return self.name