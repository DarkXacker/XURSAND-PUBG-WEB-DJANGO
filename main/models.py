from django.db import models

# Create your models here.

class Game(models.Model):
    name = models.CharField(max_length=200)
    image = models.ImageField(upload_to='games/images/')
    game = models.FileField(upload_to='games/games/')
    video = models.FileField(upload_to='games/videos/', blank=True)

    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-date']

    def __str__(self):
        return self.name