from django.contrib.gis import admin
from leaflet.admin import LeafletGeoAdmin
from markers.models import Marker, Category, City
from .models import Denuncia

# Configuração da interface de administração para o modelo Denuncia
@admin.register(Denuncia)
class DenunciaAdmin(admin.ModelAdmin):
    list_display = ("nome_completo", "motivo", "cidade", "data_envio")  # Campos mostrados na lista
    search_fields = ("nome_completo", "motivo", "cidade")  # Campos disponíveis para pesquisa

# Configuração da interface de administração para o modelo Marker usando LeafletGeoAdmin
@admin.register(Marker)
class MarkerAdmin(LeafletGeoAdmin):
    list_display = ("name", "description", "location", "categories", "city", "icon_choice")
    search_fields = ("name", "description")

# Configuração da interface de administração para o modelo Category
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("category_name",)
    search_fields = ("category_name",)

# Configuração da interface de administração para o modelo City
@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ("name",)
