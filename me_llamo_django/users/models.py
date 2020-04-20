from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone
from django.urls import reverse
from PIL import Image


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')
    new_card_number = models.PositiveIntegerField(default=8)
    last_card_generaterd = models.DateField(null=True, blank=True)

    def __str__(self):
        return f'{self.user.username} Profile'

    def get_absolute_url(self):
        return reverse('profile', kwargs={'pk': self.pk})

    def save(self, *args, **kwargs):
            super().save(*args, **kwargs)
            img = Image.open(self.image.path)
            if img.height > 300 or img.width > 300:
                output_size = (300,300)
                img.thumbnail(output_size)
                img.save(self.image.path)





