from django.contrib.admin import *
from django.contrib.auth.models import User, Group
from django.contrib.sites.models import Site
from modeltranslation.admin import TranslationAdmin
from .models import Event

site.unregister(User)
site.unregister(Group)
site.unregister(Site)

@register(Event)
class EventAdmin(TranslationAdmin):

	list_display = ('id', 'title', 'date', 'time')
	list_display_links = ('id', 'title', 'date', 'time')
	ordering = ('-date',)

	# class Media:
	# 	js = (
    #         'http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',
    #         'http://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js',
    #         'modeltranslation/js/tabbed_translation_fields.js',
    #     )
	# 	css = {
    #         'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
    #     }