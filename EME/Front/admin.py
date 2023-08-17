from django.contrib import admin
from Front.models import Banner

@admin.register(Banner)
class Banner(admin.ModelAdmin):
    list_display = ("logo", "theme_of_year", "description", "bible_verse", "background_image", "created" )
    