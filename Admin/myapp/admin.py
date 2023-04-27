from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register([MedicalCamp_event,
                     Bloodcamp_event,
                     Educational_event,
                     CBEmodel,
                     AnimalCampModel,
                     ForScribersModel,
                     ApplicantsModel])