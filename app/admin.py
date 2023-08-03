from django.contrib.admin import *
from .models import Event

@register(Event)
class EventAdmin(ModelAdmin):

	list_display = ('id', 'title', 'date',)
	list_display_links = ('id', 'title', 'date',)
	ordering = ('-date',)