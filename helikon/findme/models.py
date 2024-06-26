from django.db import models


class CarListing(models.Model):
    website = models.URLField()
    country = models.CharField(max_length=100)
    type = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.website} - {self.country} - {self.type}"
