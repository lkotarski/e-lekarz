from django.db import models
from django.conf import settings
from django.core.validators import MaxValueValidator, MinValueValidator
from django.contrib.auth.models import AbstractUser
from django.forms import ChoiceField
from datetime import time

class CustomUser(AbstractUser):
    #AbstractUser already holds first- and lastname, as well as email
    second_name = models.CharField(max_length=50, blank=True, null=True, verbose_name="Drugie imię")
    PESEL = models.IntegerField(unique=True, validators=[MinValueValidator(90000000000),MaxValueValidator(99999999999)])
    city = models.CharField(max_length=50, verbose_name="Miasto")
    address = models.CharField(max_length=255, verbose_name="Adres zamieszkania")
    phone_number = models.IntegerField(verbose_name="Numer telefonu", unique=True, validators=[MinValueValidator(100000000),MaxValueValidator(999999999)])
    isDoctor = models.BooleanField(default=False)

class DoctorProfile(models.Model):

    SPECS = [
        ("kardiolog", "Kardiolog"), ("kardiochirurg", "Kardiochirurg"),
        ("ortopeda", "Ortopeda"), ("fizjoterapeuta", "Fizjoterapeuta"),
        ("psycholog", "Psycholog"),  ("psychoterapeuta", "Psychoterapeuta"),
        ("psychiatra", "Psychiatra"),  ("psychiatra_dziecięcy", "Psychiatra dziecięcy"),
        ("weterynarz", "Weterynarz"),  ("pediatra", "Pediatra"),
        ("hepatolog", "Hepatolog"),  ("nefrolog", "Nefrolog"),
        ("stomatolog", "Stomatolog"),  ("dermatolog", "Dermatolog"),
        ("neurolog", "Neurolog"),  ("neurochirurg", "Neurochirurg"),
        ("chirurg", "Chirurg"),  ("kardiochirurg", "Kardiochirurg"),
        ("hematolog", "Hematolog"),  ("laryngolog", "Laryngolog"),
        ("alergolog", "Alergolog"),  ("pulmunolog", "Pulmunolog"),
        ("anestezjolog", "Anestezjolog"),  ("lekarz_rodzinny", "Lekarz rodzinny"),
        ("lekarz_medycyny_pracy", "Lekarz medycyny pracy"),  ("gastrolog", "Gastrolog"),
        ("ginekolog", "Ginekolog"),  ("endokrynolog", "Endokrynolog"),
    ]

    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='doctor_profile', primary_key=True)
    description = models.TextField(verbose_name="Opis")
    PWZ_number = models.IntegerField(blank=True, null=True, verbose_name="Numer licencji lekarskiej", unique=True, validators=[MinValueValidator(100000),MaxValueValidator(999999)])
    facility = models.CharField(max_length=255, verbose_name="Placówka")
    city = models.CharField(max_length=50, verbose_name="Miasto")
    address = models.CharField(max_length=255, verbose_name="Adres") 
    spec1 = models.CharField(max_length=50, choices=(SPECS), verbose_name="Główna specjalizacja") #choice
    spec2 = models.CharField(max_length=50, choices=(SPECS), blank=True, null=True, verbose_name="Dodatkowa specjalizacja (opcjonalna)") #choice

    def get_absolute_url(self):
        from django.urls import reverse
        return reverse('main:docProfile', kwargs={'id':self.user.id})

class Appointment(models.Model):

    HOURS = [
        (time(8, 00), "8:00"), (time(8, 30), "8:30"),
        (time(9, 00), "9:00"), (time(9, 30), "9:30"),
        (time(10, 00), "10:00"), (time(10, 30), "10:30"),
        (time(11, 00), "11:00"), (time(11, 30), "11:30"),
        (time(12, 00), "12:00"), (time(12, 30), "12:30"),
        (time(13, 00), "13:00"), (time(13, 30), "13:30"),
        (time(14, 00), "14:00"), (time(14, 30), "14:30"),
        (time(15, 00), "15:00"), (time(15, 30), "15:30"),
        (time(16, 00), "16:00"), (time(16, 30), "16:30"),
        (time(17, 00), "17:00"), (time(17, 30), "17:30"),
        (time(18, 00), "18:00"), (time(18, 30), "18:30"),
        (time(19, 00), "19:00"), (time(19, 30), "19:30"),
        (time(20, 00), "20:00"), (time(20, 30), "20:30")        
    ]

    patient = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="patient", null=True, blank=True)
    doctor = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="doc")
    
    first_name = models.CharField(max_length=30, verbose_name="Imię", null=True, blank=True)
    last_name = models.CharField(max_length=50, verbose_name="Nazwisko", null=True, blank=True)
    phone_number = models.IntegerField(verbose_name="Numer telefonu", null=True, blank=True)
    
    date = models.DateField(verbose_name="Dzień wizyty")
    hour = models.TimeField(choices=HOURS, verbose_name="Godzina wizyty")
    cause = models.TextField(verbose_name="Powód wizyty")

class Comment(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="author")
    doctor = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="commented_doc")

    timestamp = models.DateTimeField(auto_now_add=True)
    content = models.CharField(max_length=1000, verbose_name="Treść komentarza:")

    def __str__(self) -> str:
        return f"{self.author} (id={self.author.id}) commented on {self.doctor} (id={self.doctor.id})"