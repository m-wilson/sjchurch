from django import template
from events.models import Category, Event
from events.utils import sorted_event_list

register = template.Library()


@register.assignment_tag
def get_events_categories():
    return Category.objects.all()


@register.assignment_tag
def get_events():
    return Event.objects.all().prefetch_related('recurringevent_set', 'recurringeventexclusion_set')


@register.assignment_tag
def get_upcoming_events(limit=None):
    return sorted_event_list(limit=limit)
