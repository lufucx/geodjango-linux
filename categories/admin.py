from django.contrib.gis import admin
from django.contrib import admin
from categories.models import Category, City

# Register your models here.

admin.site.register(Category)
admin.site.register(City)