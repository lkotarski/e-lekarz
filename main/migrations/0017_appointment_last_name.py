# Generated by Django 4.0.4 on 2022-06-13 01:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0016_appointment_first_name_appointment_phone_number_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='appointment',
            name='last_name',
            field=models.CharField(blank=True, max_length=30, null=True, verbose_name='Imię'),
        ),
    ]