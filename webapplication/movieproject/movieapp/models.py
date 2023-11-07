from django.db import models

# Create your models here.
class movies(models.Model):
    name=models.CharField(max_length=222)
    des=models.TextField()
    year=models.IntegerField()
    img=models.ImageField(upload_to='gallery')

    def __str__(self):
        return self.name