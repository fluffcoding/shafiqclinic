from django import forms
from .models import Patient, Disease, MedicineIntake


class PatientForm(forms.ModelForm):
    class Meta:
        model = Patient
        exclude = ('disease','prescription')


class DiseaseForm(forms.ModelForm):
    class Meta:
        model = Disease
        fields = '__all__'


class PatientDiseaseForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = ('disease',)


class MedicineIntakeForm(forms.ModelForm):
    class Meta:
        model = MedicineIntake
        fields = '__all__'

