from django.contrib import admin
from django.utils.safestring import mark_safe
from . import models 
# Register your models here.

@admin.register(models.Categorie)
class CategorieAdmin(admin.ModelAdmin):
    list_display = ('nom', 'date_add', 'date_update', 'status')
    search_fields = ('nom',)

@admin.register(models.DrinkMenu)
class DrinkMenuAdmin(admin.ModelAdmin):
    list_display = ('nom', 'description', 'prix','imagedrink','categorie', 'date_add', 'date_update', 'status')
    search_fields = ('nom',)

    def imagedrink(self, obj):
        return mark_safe(f'<img src="{obj.image.url}" style="height:50px; width:100px">')


@admin.register(models.Website)
class WebsiteAdmin(admin.ModelAdmin):
    list_display = ('logo', 'nom_site', 'titre_contact','titre_about', 'imageabout','date_add', 'date_update', 'status')


    def imageabout(self, obj):
        return mark_safe(f'<img src="{obj.image.url}" style="height:50px; width:100px">')

@admin.register(models.About)
class AboutAdmin(admin.ModelAdmin):
    list_display = ('titre', 'sous_titre', 'description','image', 'date_add', 'date_update', 'status')

    def image(self, obj):
        return mark_safe(f'<img src="{obj.image.url}" style="height:50px; width:100px">')

@admin.register(models.SpecialItems)
class SpecialItemsAdmin(admin.ModelAdmin):
    ('titre', 'description','image', 'date_add', 'date_update', 'status')

    def image(self, obj):
        return mark_safe(f'<img src="{obj.image.url}" style="height:50px; width:100px">')

@admin.register(models.Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('nom', 'email', 'message', 'date_add', 'date_update', 'status')