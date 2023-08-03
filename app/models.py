from django.db.models import *
from django.utils import timezone

class Event(Model):

	date = DateField(
		'Дата мероприятия',
		default=timezone.now
	)

	title = CharField(
		'Название мероприятия',
		max_length=256
	)

	subtitle = CharField(
		'Подзагаловок',
		max_length=256
	)

	dop_info = TextField(
		'Дополнительное поле',
		blank=True,
		null=True
	)

	def __str__(self):
		return f'{self.title}'

	class Meta:
		verbose_name = 'Событие'
		verbose_name_plural = 'События'
		ordering = ['-date']