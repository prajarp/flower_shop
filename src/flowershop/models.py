from django.db import models
from PIL import Image
import os
from io import BytesIO
from django.core.files.base import ContentFile
# Create your models here.

class Color(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name

class Flower(models.Model):
    name = models.CharField(max_length=100, unique = True, error_messages={
        'unique': 'Taki kwiat już istnieje w bazie danych.'
    })
    colors = models.ManyToManyField(Color, related_name='flowers')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField()

    def __str__(self):
        # return self.name, self.colors, self.price, self.quantity or "Unnamed Flower"
        return f"{self.name} | {self.price} zł | qty: {self.quantity} | colors: {', '.join(color.name for color in self.colors.all())}" if self.name else "Unnamed Flowerur"

class FlowerArrangement(models.Model):
    name = models.CharField(max_length=100, unique = True,)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField(default = 1)

    flowers = models.ManyToManyField(
        Flower,
        through='FlowerArrangementFlower',
        related_name='arrangements'
    )

    def __str__(self):
        return self.name



class FlowerArrangementFlower(models.Model):
    flowerArrangement = models.ForeignKey(FlowerArrangement, on_delete=models.CASCADE)
    flower = models.ForeignKey(Flower, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default = 1)

    def __str__(self):
        return f"{self.quantity} x {self.flower} in {self.flowerArrangement}"

class FlowerArrangementImage(models.Model):
    arrangement = models.ForeignKey(
        FlowerArrangement,
        on_delete=models.CASCADE,
        related_name='images'
    )
    image = models.ImageField(upload_to='arrangement_images/')
    thumbnail = models.ImageField(upload_to='arrangement_images/thumbnails/', editable=False, null = True, blank = True)
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if self.image and not self.thumbnail:
            img = Image.open(self.image)
            img.thumbnail((300, 300))

            thumb_io = BytesIO()
            img.save(thumb_io, img.format)
            thumb_name = os.path.basename(self.image.name)
            self.thumbnail.save(f"thumb_{thumb_name}", ContentFile(thumb_io.getvalue()), save=False)
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Image for {self.arrangement.name} uploaded at {self.uploaded_at}"
