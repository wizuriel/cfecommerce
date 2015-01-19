from django.contrib import admin
from products.models import Product, ProductImage

# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    data_hierarchy = 'timestamp'
    list_display = ['title', 'price', 'active', 'updated']
    search_fields = ['title', 'description']
    list_editable = ['price','active']
    list_filter = ['price', 'active']
    readonly_fields = ['updated', 'timestamp']
    prepopulated_fields = {"slug": ("title",)}
    class Meta:
        model = Product

admin.site.register(Product, ProductAdmin)
admin.site.register(ProductImage)