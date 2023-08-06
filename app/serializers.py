from rest_framework.serializers import *
from .models import Event

class EventSerializer(ModelSerializer):

	class Meta:
		model = Event
		fields = (
			'id',
			"date_uz",
			"date_ru",
			"date_en",
			"time_uz",
			"time_ru",
			"time_en",
			"title_uz",
			"title_ru",
			"title_en",
			'image',
		)
		extra_kwargs = {
		    'date': {'required': False},
		    'title': {'required': False},
		    'time': {'required': False},
		    'image': {'required': False},
		}