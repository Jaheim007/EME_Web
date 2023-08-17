from django.db import models

class Banner(models.Model):
    logo = models.ImageField()
    theme_of_year = models.CharField(max_length=255, null=True , blank=True)
    description = models.TextField(null=True , blank=True)
    bible_verse = models.CharField(max_length=255, null=True , blank=True)
    background_image = models.ImageField()
    
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.theme_of_year