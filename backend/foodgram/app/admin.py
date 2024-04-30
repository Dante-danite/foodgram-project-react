from django.contrib import admin
from .models import Ingredient, Recipe, Tag


class RecipeAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'autor'
    )
    list_filter = ('autor',)


class IngredientAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'measurement_unit'
    )
    list_filter = ('name',)


admin.site.register(Tag)
admin.site.register(Recipe, RecipeAdmin)
admin.site.register(Ingredient, IngredientAdmin)

