from django.contrib import admin
from .models import Weapons

class WeaponsAdmin(admin.ModelAdmin):
    list_display = ("weapon_name", "min_damage", "max_damage")
    prepopulated_fields = {"slug": ("weapon_name",)}

admin.site.register(Weapons, WeaponsAdmin)
