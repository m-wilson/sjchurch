from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from django.utils.translation import ugettext as _

from people.models import IndividualLink

class IndividualLink_Plugin(CMSPluginBase):
    model = IndividualLink
    name = _("Individual Link") # Name of the plugin
    render_template = "individual/individual_link_plugin.html"

    text_enabled = True
        
    def render(self, context, instance, placeholder):
        individual= instance.individual
          
        context.update({'individual': individual})

        return context

    def __unicode__(self):
        return self.model.individual

plugin_pool.register_plugin(IndividualLink_Plugin)