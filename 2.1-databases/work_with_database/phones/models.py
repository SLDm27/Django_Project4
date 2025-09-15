from django.db import models
from django.utils.text import slugify


class Phone(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=150)
    price = models.IntegerField()
    image = models.URLField()
    release_date = models.DateField()
    lte_exists = models.BooleanField(default=False)
    slug = models.SlugField()


    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)


    def __str__(self):
        return self.name

    class Phone(models.Model):
        id = models.IntegerField(primary_key=True)
        name = models.CharField(max_length=100)
        price = models.IntegerField()
        image = models.URLField()
        release_date = models.DateField()
        lte_exists = models.BooleanField(default=False)
        slug = models.SlugField()

        def __str__(self):
            return f"{self.id};" \
                   f" {self.name};" \
                   f" {self.price};" \
                   f" {self.image};" \
                   f" {self.release_date};" \
                   f" {self.lte_exists};" \
                   f" {self.slug}"