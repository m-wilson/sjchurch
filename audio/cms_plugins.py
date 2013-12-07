from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from audio.models import FilerAudioPlugin as FilerAudioPluginModel
from audio.models import AudioListPlugin as AudioListPluginModel
from audio.models import FilerAudioFile

from django.utils.translation import ugettext as _


class FilerAudioPlugin(CMSPluginBase):
    model = FilerAudioPluginModel # Model where data about this plugin is saved
    name = _("Audio") # Name of the plugin
    render_template = "audio/plugin.html" # template to render the plugin with

    def render(self, context, instance, placeholder):
        context.update({'instance':instance})
        return context

plugin_pool.register_plugin(FilerAudioPlugin) # register the plugin

class AudioListPlugin(CMSPluginBase):
    model = AudioListPluginModel # Model where data about this plugin is saved
    name = _("Audio List") # Name of the plugin
    render_template = "audio/pluginList.html" # template to render the plugin with

    def render(self, context, instance, placeholder):
        n= instance.number_of_audiofiles
        audio_list= FilerAudioFile.objects.order_by('date')[:n]

        context.update({'audio_list': audio_list})
        return context

plugin_pool.register_plugin(AudioListPlugin) # register the plugin
