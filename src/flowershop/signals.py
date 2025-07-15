import os
from django.db.models.signals import post_delete
from django.dispatch import receiver
from .models import FlowerArrangementImage

@receiver(post_delete, sender=FlowerArrangementImage)
def delete_image_file(sender, instance, **kwargs):
    if instance.image:
        if os.path.isfile(instance.image.path):
            os.remove(instance.image.path)
