# Generated by Django 4.0.4 on 2022-06-13 02:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0017_appointment_last_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment',
            name='last_name',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Nazwisko'),
        ),
    ]
