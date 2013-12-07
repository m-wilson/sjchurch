from django.utils import timezone
from events.models import Event, DAY_CHOICES
from dateutil import rrule
from dateutil.relativedelta import relativedelta
from zinnia.models import Category

def sorted_event_list(start_date=None, end_date=None, limit=None, specified_categories= None):
    # Default start date
    if start_date is None:
        start_date = timezone.now()

    # Default end date
    if end_date is None:
        end_date = start_date + relativedelta(months=+12)

    # Need matching naive versions
    current_zone = timezone.get_default_timezone()
    start_date_naive = timezone.make_naive(start_date, current_zone)
    end_date_naive = timezone.make_naive(end_date, current_zone)

    event_list = []
    if specified_categories is None:
        for event in Event.objects.all().prefetch_related('recurringevent_set', 'recurringeventexclusion_set'):
            if event.recurringevent_set.all():
                # Recurring event
                for i in event.recurringevent_set.all():
                    event_ruleset = rrule.rruleset()
                    event_ruleset.rrule(i.rrule())
    
                    # Add in any exclusions
                    for j in event.recurringeventexclusion_set.all():
                        event_ruleset.exdate(timezone.make_naive(j.date, current_zone))
    
                    # Only add dates in the period we're viewing
                    for j in event_ruleset.between(start_date_naive, end_date_naive):
                        event_occurance_tz = timezone.make_aware(j, current_zone)
                        event_list.append((event_occurance_tz, event))
            else:
                # One off event
                if end_date > event.start > start_date: # Bug in source code had reversed start_date and end_date in inequality. Fixed here.
                    event_list.append((event.start, event, DAY_CHOICES[event.start.weekday()][1], event.end.time()))
    else:
        for event in Event.objects.filter(category__eventcategory__in=specified_categories).prefetch_related('recurringevent_set', 'recurringeventexclusion_set').distinct():
            if event.recurringevent_set.all():
                # Recurring event
                for i in event.recurringevent_set.all():
                    event_ruleset = rrule.rruleset()
                    event_ruleset.rrule(i.rrule())
    
                    # Add in any exclusions
                    for j in event.recurringeventexclusion_set.all():
                        event_ruleset.exdate(timezone.make_naive(j.date, current_zone))
    
                    # Only add dates in the period we're viewing
                    for j in event_ruleset.between(start_date_naive, end_date_naive):
                        event_occurance_tz = timezone.make_aware(j, current_zone)
                        event_list.append((event_occurance_tz, event))
            else:
                # One off event
                if end_date > event.start > start_date: # Bug in source code had reversed start_date and end_date in inequality. Fixed here.
                    event_list.append((event.start, event, DAY_CHOICES[event.start.weekday()][1], event.end.time()))
    # Sort by date
    event_list.sort(key=lambda x: x[0])

    # Limited number of events
    if limit is not None:
        event_list = event_list[:limit]

    return event_list
