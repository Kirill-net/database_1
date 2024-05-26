from django.db import models


class Phone(models.Model):

    name = models.CharField(max_length=200)
    price = models.IntegerField()
    image = models.URLField(max_length=200)
    release_date = models.DateField()
    lte_exists = models.BooleanField()
    slug = models.SlugField(max_length=100, unique=True)
