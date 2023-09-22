from django.db import models


class Movie(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    release_date = models.DateField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    mda = models.CharField(max_length=5, null=True, blank=True)

    def __str__(self):
        return self.title
