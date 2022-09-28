from django.contrib import admin
from .models import CustomUser, DoctorProfile, Comment, Appointment

admin.site.register(CustomUser)
admin.site.register(DoctorProfile)
admin.site.register(Comment)
admin.site.register(Appointment)