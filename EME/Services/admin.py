from django.contrib import admin
from Services.models import Sermons , Features , Church_Service

@admin.register(Church_Service)
class Church_Service(admin.ModelAdmin):
    list_display = ("title" , "description" , "day" , "time" , "created" , "updated")
    
@admin.register(Features)
class Features(admin.ModelAdmin):
    list_display = ("icons" , "title", "description")
    
@admin.register(Sermons)
class Sermons(admin.ModelAdmin):
    list_display = ("title" , "preacher" , "mini_title" , "description")

# Register your models here.
