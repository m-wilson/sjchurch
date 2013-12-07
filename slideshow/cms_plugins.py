from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from slideshow.models import SlideshowPlugin
from django.utils.translation import ugettext as _
from django.conf import settings
import os

class SlideshowCMSPlugin(CMSPluginBase):
    model = SlideshowPlugin # Model where data about this plugin is saved
    name = _("Slideshow") # Name of the plugin
        
    render_template = 'slideshow/slideshow_plugin.html'

    def render(self, context, instance, placeholder):
        no_of_images= len(instance.model.images.all())
        imageUrl= {}
        imageCaption= {}
        for imageNo in range(no_of_images):
            #The following lines append the dictionaries
            imageUrl[imageNo]= instance.model.images.all()[imageNo].image.url
            imageCaption[imageNo]= instance.model.images.all()[imageNo].caption
        
        slideshow_name= instance.model.name
            
        context.update({
                        'canvas_width': instance.width,
                        'canvas_height': instance.height,
                        'pause_duration': instance.pause_duration,
                        'no_of_images': no_of_images,
                        'range': range(no_of_images),
                        'image_urls': imageUrl,
                        'image_captions': imageCaption,
                        'slideshow_name': slideshow_name
                        })
        return context

plugin_pool.register_plugin(SlideshowCMSPlugin) # register the plugin