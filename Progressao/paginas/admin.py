from django.contrib import admin

# Register your models here.
from .models import Entitie


@admin.register(Entitie)
class EntitiesAdmin(admin.ModelAdmin):
    verbose_name = 'Categorie'


from .models import Villain


@admin.register(Villain)
class VillainAdmin(admin.ModelAdmin):
    verbose_name = 'Villain'

# Register your models here.
