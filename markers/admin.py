from django.contrib.gis import admin
from leaflet.admin import LeafletGeoAdmin
from markers.models import Marker, Category, City
from .models import Denuncia

@admin.register(Denuncia)
class DenunciaAdmin(admin.ModelAdmin):
    list_display = ("nome_completo", "motivo", "cidade", "data_envio")
    search_fields = ("nome_completo", "motivo", "cidade")

@admin.register(Marker)
class MarkerAdmin(LeafletGeoAdmin):
    list_display = ("name", "description", "location", "categories", "city", "icon_choice")
    search_fields = ("name", "description")

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("category_name",)
    search_fields = ("category_name",)


@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ("name",)