from django.contrib import admin

from .models import Patient, MedicineIntake, Disease, Medicine

admin.site.register(Patient)
admin.site.register(Disease)
admin.site.register(Medicine)
admin.site.register(MedicineIntake)
