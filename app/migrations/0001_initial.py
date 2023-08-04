# Generated by Django 4.2.4 on 2023-08-04 12:49

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(default=django.utils.timezone.now, verbose_name='Дата мероприятия')),
                ('title', models.CharField(max_length=256, verbose_name='Название мероприятия')),
                ('subtitle', models.CharField(max_length=256, verbose_name='Подзагаловок')),
                ('dop_info', models.TextField(blank=True, null=True, verbose_name='Дополнительное поле')),
                ('image', models.ImageField(upload_to='events-photos/%Y/%m/%d', verbose_name='Фото')),
            ],
            options={
                'verbose_name': 'Событие',
                'verbose_name_plural': 'События',
                'ordering': ['-date'],
            },
        ),
    ]
