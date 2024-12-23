from django.db import models

class Location(models.Model):
    timestamp = models.DateTimeField(auto_now_add=True)
    latitude = models.FloatField()
    longitude = models.FloatField()
    what3words = models.CharField(max_length=255)

    def __str__(self):
        return self.what3words
