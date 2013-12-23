from django.db import models
from cms.models import CMSPlugin
from filer.fields.image import FilerImageField
from django.contrib import admin
    
class SlideshowImage(models.Model):
    name= models.CharField(max_length= 200)
    image= FilerImageField(null= True, blank= True, related_name="image")
    caption= models.CharField(max_length= 200)
    
    def __unicode__(self):
        return self.name    
    
class Slideshow(models.Model):
    name= models.CharField(max_length= 200)

    images= models.ManyToManyField(SlideshowImage)
    
    def __unicode__(self):
        return self.name
    
class SlideshowPlugin(CMSPlugin):
    model= models.ForeignKey(Slideshow)
    name= u'Slideshow'
    width= models.IntegerField(default= 512)
    height= models.IntegerField(default= 128)
    pause_duration= models.IntegerField(default= 8000)
    
    
    def __unicode__(self):
        return self.model.name
    

admin.site.register(Slideshow)
admin.site.register(SlideshowImage)

