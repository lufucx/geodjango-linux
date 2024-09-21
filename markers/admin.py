from django.contrib.gis import admin
from leaflet.admin import LeafletGeoAdmin
from markers.models import Marker, Category, City
from .models import Denuncia

# Configuração da interface de administração para o modelo Denuncia
@admin.register(Denuncia)
class DenunciaAdmin(admin.ModelAdmin):
    list_display = ("nome_completo", "motivo", "cidade", "data_envio")  # Campos mostrados na lista
    search_fields = ("nome_completo", "motivo", "cidade")  # Campos disponíveis para pesquisa

    # Impedir adição de novos registros
    def has_add_permission(self, request):
        return False

    # Impedir a edição de registros
    def has_change_permission(self, request, obj=None):
        return False

    # Permitir exclusão de registros
    def has_delete_permission(self, request, obj=None):
        return True

    # Tornar todos os campos somente leitura
    def get_readonly_fields(self, request, obj=None):
        if obj:  # Para um objeto existente, todos os campos serão somente leitura
            return [f.name for f in obj._meta.fields]
        return super().get_readonly_fields(request, obj)


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
