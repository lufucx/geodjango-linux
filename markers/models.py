from django.contrib.gis.db import models


class Marker(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    location = models.PointField()
    hyperlink = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.name