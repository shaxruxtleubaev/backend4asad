from django.contrib.admin import *
from django.contrib.auth.models import User, Group
from django.contrib.sites.models import Site
from .models import Event

site.unregister(User)
site.unregister(Group)
site.unregister(Site)

@register(Event)
class EventAdmin(ModelAdmin):

	list_display = ('id', 'title', 'date',)
	list_display_links = ('id', 'title', 'date',)
	ordering = ('-date',)