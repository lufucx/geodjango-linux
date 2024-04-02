from django.contrib.gis.db import models
from categories.models import Category, City

class Marker(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    categories = models.ForeignKey(Category, on_delete=models.CASCADE, default=1)
    city = models.ForeignKey(City, on_delete=models.CASCADE, default=1)
    location = models.PointField()
    hyperlink = models.URLField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
