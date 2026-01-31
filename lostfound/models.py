from django.conf import settings
from django.db import models


class LostFoundItem(models.Model):
    class Status(models.TextChoices):
        LOST = 'lost', 'Lost'
        FOUND = 'found', 'Found'
        RETURNED = 'returned', 'Returned'

    title = models.CharField(max_length=200)
    description = models.TextField()
    status = models.CharField(max_length=10, choices=Status.choices, default=Status.LOST)
    location = models.CharField(max_length=200)
    image = models.ImageField(upload_to='lostfound/', blank=True, null=True)
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='lostfound_items'
    )
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self) -> str:
        return self.title

# Create your models here.
