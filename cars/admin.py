from django.contrib import admin
from .models import car
from django.utils.html import format_html
# Register your models here.
class AdminCars(admin.ModelAdmin):
    def thumbnail(self,object):
        return format_html('<img src="{}" width="40" style="border-radius: 100px;" />'.format(object.car_photo.url))

    thumbnail.short_description = 'Car Photo'
    list_display = ('car_title','city' ,'thumbnail' ,'color', 'model', 'year', 'body_style', 'fuel_type', 'is_featured')
    list_display_links = ('thumbnail','car_title')
    list_editable = ('is_featured',)
    search_fields = ('car_title','city','model')
    list_filter = ('car_title','city','color', 'model', 'fuel_type')

admin.site.register(car,AdminCars)