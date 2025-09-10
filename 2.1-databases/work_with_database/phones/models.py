from django.db import models


class Phone(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length= 254, null=False)
    price = models.IntegerField(default=None)
    image = models.URLField(default=None)
    release_date = models.DateField(default=None)
    lte_exists = models.BooleanField(default=None)
    slug = models.SlugField(max_length = 200)


    def __str__(self):
        return f'{self.id}. {self.name}'