from django.db.models import *
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

class Event(Model):

	date = CharField(
		_('Sana'),
		max_length=256
	)

	time = CharField(
		_('Vaqt'),
		max_length=256
	)

	title = CharField(
		_('Konsert nomi'),
		max_length=256
	)

	image = ImageField(
		'Fotosurat',
		upload_to='events-photos/%Y/%m/%d'
	)

	def __str__(self):
		return f'{self.title}'

	class Meta:
		verbose_name = 'Konsert'
		verbose_name_plural = 'Konsertlar'
		ordering = ['-date']