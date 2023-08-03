from django.shortcuts import render
from rest_framework.permissions import *
from rest_framework.viewsets import *
from .models import Event
from .serializers import EventSerializer

class EventViewSet(ModelViewSet):
	permission_classes = (AllowAny,)
	queryset = Event.objects.all()
	serializer_class = EventSerializer