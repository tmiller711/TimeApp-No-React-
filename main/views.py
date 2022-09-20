from datetime import datetime, timedelta, date
from django.shortcuts import render, HttpResponseRedirect, get_object_or_404
from django.http import HttpResponse
from django.views import generic
from django.utils.safestring import mark_safe
from calendar import HTMLCalendar
from django.urls import reverse

from .models import *
from .utils import Calendar
from .forms import EventForm

# class CalendarView(generic.ListView):
#     model = Event
#     template_name = 'main/calendar.html'

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         d = get_date(self.request.GET.get('month', None))
#         today = datetime.today()
#         cal = Calendar(d.year, d.month)
#         html_cal = cal.formatmonth(withyear=True)
#         context['calendar'] = mark_safe(html_cal)
#         context['prev_month'] = cal.prev_month(d)
#         context['next_month'] = cal.next_month(d)
#         # print(html_cal)
#         return context

def calendar_view(request):
    d = get_date(request.GET.get('month', None))
    today = datetime.today()
    cal = Calendar(d.year, d.month)
    html_cal = cal.formatmonth(withyear=True)
    calendar = mark_safe(html_cal)
    prev_month = cal.prev_month(d)
    next_month = cal.next_month(d)
    # print(html_cal)
    print(request.user)
    return render(request, 'main/calendar.html', {'calendar': calendar, 'prev_month': prev_month, 'next_month': next_month})

# if there is an event_id we want to use that object and if it doesn't we want a new object
def event(request, event_id=None):
    instance = Event()
    if event_id:
        instance = get_object_or_404(Event, pk=event_id)
    else:
        instance = Event()

    form = EventForm(request.POST or None, instance=instance)
    if request.POST and form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse('cal:calendar'))
    return render(request, 'main/event.html', {'form': form})


def day(request, year, month, day):
    date = str(year) + '-' + str(month) + '-' + str(day)
    return render(request, 'main/day.html', {'date': date})


def get_date(req_day):
    if req_day:
        year, month = (int(x) for x in req_day.split('-'))
        return date(year, month, day=1)
    return datetime.today()

