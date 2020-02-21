from django.contrib import admin
# Register your models here.
from .import models
from.models import Category,Product
from django.contrib.admin.options import ModelAdmin

# Register your models here.
class CategoryAdmin(ModelAdmin):
    list_display = ['name','slug']
    prepopulated_fields={'slug':('name',)}

class ProductAdmin(ModelAdmin):
    list_display=['name','slug','category','price','stock','available','created','updated']
    list_filter=['created','updated','category']
    prepopulated_fields={'slug':('name',)}   

admin.site.register(models.Category,CategoryAdmin)
admin.site.register(models.Product,ProductAdmin)  
