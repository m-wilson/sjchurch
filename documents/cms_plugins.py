from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from documents.models import DocumentListPlugin as DocumentListPluginModel
#from documents.models import FilerDocumentPlugin
from documents.models import FilerDocumentFile

from django.utils.translation import ugettext as _

# class FilerDocumentPlugin(CMSPluginBase):
#     model = FilerDocumentPlugin # Model where data about this plugin is saved
#     name = _("Document") # Name of the plugin
#     render_template = "documents/plugin.html" # template to render the plugin with
#  
#     def render(self, context, instance, placeholder):
#         context.update({'instance':instance})
#         return context
 
#plugin_pool.register_plugin(FilerDocumentPlugin) # register the plugin

class DocumentListPlugin(CMSPluginBase):
    model = DocumentListPluginModel # Model where data about this plugin is saved
    name = _("Document List") # Name of the plugin
    render_template = "documents/pluginList.html" # template to render the plugin with

    def render(self, context, instance, placeholder):
        n= instance.number_of_documents
        doc_cat= instance.category
        document_list= FilerDocumentFile.objects.all().filter(category__exact=doc_cat).order_by('date')[:n]

        context.update({'document_list': document_list})
        return context

plugin_pool.register_plugin(DocumentListPlugin) # register the plugin