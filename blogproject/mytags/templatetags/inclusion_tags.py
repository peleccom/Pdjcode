from django import template
from django.utils import timezone
from django.conf import settings
register = template.Library()

@register.inclusion_tag("_calendar.html")
def calendar_table():
    import calendar
    date = timezone.now()
    month = calendar.monthcalendar(date.year, date.month)
    weeks = [[day or '' for day in week] for week in month]
    print calendar.month_name[date.month]
    return {
        'month': calendar.month_name[date.month],
        'year': date.year,
        'weeks': weeks,
        'daynames': calendar.day_abbr,}