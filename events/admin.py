from django.contrib import admin
from events.models import Category, Event

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ("date", "name", "sub_title", "slug", "category", "category_slug") # Uebersichtsseite
    prepopulated_fields = {"slug": ("name",)}
    list_display_links = ("date", "name", "sub_title")
    search_fields = ("name", "sub_title")
    list_filter = ("category", )

    def category_slug(self, obj):
        return obj.category.slug

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "sub_title", "slug") # Uebersichtsseite
    prepopulated_fields = {"slug": ("name",)}
    list_display_links = ("id", "name", "sub_title")
    search_fields = ("name", "sub_title")
    list_filter = ("events", "sub_title")
