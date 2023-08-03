from rest_framework.serializers import *
from .models import Event

class EventSerializer(ModelSerializer):

	class Meta:
		model = Event
		fields = '__all__'
		extra_kwargs = {
		    'date': {'required': False},
		    'title': {'required': False},
		    'subtitle': {'required': False},
		    'dop_info': {'required': False},
		}