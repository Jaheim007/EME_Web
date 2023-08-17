from django.db import models

class Church_Service(models.Model):
    title = models.CharField(max_length=255 , null=True , blank=True)
    description = models.TextField(null=True , blank=True)
    day = models.CharField(max_length=255, null=True , blank=True)
    time = models.CharField(max_length=255, null=True , blank=True)
    
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    
    
    def __str__(self):
        return self.title
    
class Features(models.Model):
    icons = models.CharField(max_length=255, null=True , blank=True)
    title = models.CharField(max_length=255, null=True , blank=True)
    description = models.TextField(null=True , blank=True)
    
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    
    
    def __str__(self):
        return self.icons
    
class Sermons(models.Model):
    title = models.CharField(max_length=255, null=True , blank=True)
    preacher = models.CharField(max_length=255, null=True , blank=True)
    mini_title = models.CharField(max_length=255, null=True , blank=True)
    description = models.TextField(null=True , blank=True)
    
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.title
    

    

    
    