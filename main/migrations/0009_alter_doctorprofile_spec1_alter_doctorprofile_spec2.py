# Generated by Django 4.0.4 on 2022-06-12 14:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_alter_doctorprofile_spec1_alter_doctorprofile_spec2'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctorprofile',
            name='spec1',
            field=models.CharField(choices=[('kardiolog', 'Kardiolog'), ('kardiochirurg', 'Kardiochirurg'), ('ortopeda', 'Ortopeda'), ('fizjoterapeuta', 'Fizjoterapeuta'), ('psycholog', 'Psycholog'), ('psychoterapeuta', 'Psychoterapeuta'), ('psychiatra', 'Psychiatra'), ('psychiatra_dziecięcy', 'Psychiatra dziecięcy'), ('weterynarz', 'Weterynarz'), ('pediatra', 'Pediatra'), ('hepatolog', 'Hepatolog'), ('nefrolog', 'Nefrolog'), ('stomatolog', 'Stomatolog'), ('dermatolog', 'Dermatolog'), ('neurolog', 'Neurolog'), ('neurochirurg', 'Neurochirurg'), ('chirurg', 'Chirurg'), ('kardiochirurg', 'Kardiochirurg'), ('hematolog', 'Hematolog'), ('laryngolog', 'Laryngolog'), ('alergolog', 'Alergolog'), ('pulmunolog', 'Pulmunolog'), ('anestezjolog', 'Anestezjolog'), ('lekarz_rodzinny', 'Lekarz rodzinny'), ('lekarz_medycyny_pracy', 'Lekarz medycyny pracy'), ('gastrolog', 'Gastrolog'), ('ginekolog', 'Ginekolog'), ('endokrynolog', 'Endokrynolog')], max_length=50),
        ),
        migrations.AlterField(
            model_name='doctorprofile',
            name='spec2',
            field=models.CharField(blank=True, choices=[('kardiolog', 'Kardiolog'), ('kardiochirurg', 'Kardiochirurg'), ('ortopeda', 'Ortopeda'), ('fizjoterapeuta', 'Fizjoterapeuta'), ('psycholog', 'Psycholog'), ('psychoterapeuta', 'Psychoterapeuta'), ('psychiatra', 'Psychiatra'), ('psychiatra_dziecięcy', 'Psychiatra dziecięcy'), ('weterynarz', 'Weterynarz'), ('pediatra', 'Pediatra'), ('hepatolog', 'Hepatolog'), ('nefrolog', 'Nefrolog'), ('stomatolog', 'Stomatolog'), ('dermatolog', 'Dermatolog'), ('neurolog', 'Neurolog'), ('neurochirurg', 'Neurochirurg'), ('chirurg', 'Chirurg'), ('kardiochirurg', 'Kardiochirurg'), ('hematolog', 'Hematolog'), ('laryngolog', 'Laryngolog'), ('alergolog', 'Alergolog'), ('pulmunolog', 'Pulmunolog'), ('anestezjolog', 'Anestezjolog'), ('lekarz_rodzinny', 'Lekarz rodzinny'), ('lekarz_medycyny_pracy', 'Lekarz medycyny pracy'), ('gastrolog', 'Gastrolog'), ('ginekolog', 'Ginekolog'), ('endokrynolog', 'Endokrynolog')], max_length=50, null=True),
        ),
    ]
