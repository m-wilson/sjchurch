from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from zinnia.models import Category
from django.utils.translation import ugettext as _

from models import Event, UpcomingEvents
from utils import sorted_event_list

class UpcomingEvents_Plugin(CMSPluginBase):
    model = UpcomingEvents
    name = _("Upcoming Events") # Name of the plugin
    render_template = "events/events_plugin.html"
    
    def render(self, context, instance, placeholder):
        include_categories= instance.categories.all()
        # NB sorted_event_list is a list of 3-tuples (instance date, event, WEEKDAY)  ***************
        upcomingEventsList= sorted_event_list(limit= instance.number_of_events, specified_categories=include_categories) # defaults to all events in the year starting now
            
        context.update({'upcoming_events': upcomingEventsList}) 
        return context

plugin_pool.register_plugin(UpcomingEvents_Plugin)