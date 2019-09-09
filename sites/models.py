from django.db import models

# Create your models here.
class Cards(models.Model):
    title = models.CharField(max_length=20)
    slug = models.SlugField()
    text = models.TextField()
    image = models.FileField(default='hills.png', blank=True)
    # adjusted
    # ad

    def __str__(self):
        return self.title



class Website(models.Model):
    title = models.CharField(max_length=20)
    slug = models.SlugField()
    image = models.FileField(default='hills.png', blank=True)

    def __str__(self):
        return self.title
