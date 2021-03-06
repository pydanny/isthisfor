from django.contrib import admin

from pitch.models import Pitch, Comment

class PitchAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'pub_date')
    prepopulated_fields = {"slug": ("name",)}
    save_on_top = True
    search_fields = ['name']

admin.site.register(Pitch, PitchAdmin)
admin.site.register(Comment)
