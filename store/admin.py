from django.contrib import admin

from store.models import (
    Category, Product, Gallery, Feature
)


class GalleryInline(admin.TabularInline):
    model = Gallery


class FeatureInline(admin.TabularInline):
    model = Feature


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'active')
    list_filter = ['active']
    search_fields = ['title']


class ProductAdmin(admin.ModelAdmin):
    list_display = ('title',)
    list_filter = ['active']
    search_fields = ['title']
    inlines = [GalleryInline, FeatureInline]


admin.site.register(Category, CategoryAdmin)


admin.site.register(Product, ProductAdmin)
