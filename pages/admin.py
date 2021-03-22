from django.contrib import admin
from pages.models import Team
from django.utils.html import format_html

# Register your models here.
class AdminTeams(admin.ModelAdmin):
    def image(self,object):
        return format_html('<img src="{}" width="40" style="border-radius: 100px;" />'.format(object.photo.url))

    image.short_description = 'Photo'
    list_filter = ('designation',)
    list_display = ('id','image','first_name','last_name','photo')
    list_display_links = ('id','image','first_name',)
    search_fields = ('first_name','last_name')
admin.site.register(Team,AdminTeams)