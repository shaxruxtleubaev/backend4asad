from django.db.models import *
from django.utils import timezone

class Event(Model):

	date = CharField(
		'Дата',
		max_length=256
	)

	time = CharField(
		'Время',
		max_length=256
	)

	title = CharField(
		'Название мероприятия',
		max_length=256
	)

	image = ImageField(
		'Фото',
		upload_to='events-photos/%Y/%m/%d'
	)

	def __str__(self):
		return f'{self.title}'

	class Meta:
		verbose_name = 'Событие'
		verbose_name_plural = 'События'
		ordering = ['-date']