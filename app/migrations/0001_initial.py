# Generated by Django 4.2.4 on 2023-08-05 19:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.CharField(max_length=256, verbose_name='Дата')),
                ('time', models.CharField(max_length=256, verbose_name='Время')),
                ('title', models.CharField(max_length=256, verbose_name='Название мероприятия')),
                ('image', models.ImageField(upload_to='events-photos/%Y/%m/%d', verbose_name='Фото')),
            ],
            options={
                'verbose_name': 'Событие',
                'verbose_name_plural': 'События',
                'ordering': ['-date'],
            },
        ),
    ]
