from django.contrib import admin

from .models import Patient, MedicineIntake, Disease

admin.site.register(Patient)
admin.site.register(MedicineIntake)
admin.site.register(Disease)