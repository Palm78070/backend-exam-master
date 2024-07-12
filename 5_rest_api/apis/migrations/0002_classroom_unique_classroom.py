# Generated by Django 5.0.4 on 2024-07-12 18:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apis', '0001_initial'),
    ]

    operations = [
        migrations.AddConstraint(
            model_name='classroom',
            constraint=models.UniqueConstraint(fields=('year', 'room_number', 'school'), name='unique_classroom'),
        ),
    ]