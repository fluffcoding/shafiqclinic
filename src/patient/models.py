from django.db import models

genders = {
    ('M','Male'),
    ('F','Female'),
}

medicine_quantity = {
    ('1','One Time'),
    ('2','Two Time'),
    ('3','Three Time'),
}

class Patient(models.Model):
    name = models.CharField(max_length=50)
    age = models.IntegerField()
    phone_number = models.IntegerField()
    gender = models.CharField(choices=genders,max_length=1)
    disease = models.ManyToManyField("Disease", blank=True)
    created = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    #prescription = models.ManyToManyField("MedicineIntake", blank=True)


    def __str__(self):
        return self.name



class Disease(models.Model):
    name = models.CharField(max_length=50)


    def __str__(self):
        return self.name
    

class MedicineIntake(models.Model):
    medicine = models.CharField(max_length=100, blank=True, null=True)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, null=True, blank=True)
    disease = models.ForeignKey(Disease, on_delete=models.CASCADE, null=True, blank=True)
    dose = models.CharField(max_length=20)
    quantity = models.CharField(choices=medicine_quantity, max_length=5)
    duration = models.IntegerField()


    def __str__(self):
        return str(self.medicine.name) + " - " + str(self.medicine.company)  + " - " + self.quantity   + " times a day - " + self.dose  + " - " + str(self.duration) + " days."


'''
class Prescription(models.Model):
    medicine = models.ManyToManyField(MedicineIntake)
    time_created = models.DateTimeField(auto_now_add=True, null=True, blank=True)
'''