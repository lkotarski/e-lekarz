# Generated by Django 4.0.4 on 2022-06-06 09:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_remove_doctorprofile_id_alter_appointment_doctor_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctorprofile',
            name='spec2',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]