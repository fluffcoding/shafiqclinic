# Generated by Django 3.1 on 2020-09-07 03:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('patient', '0011_auto_20200817_1941'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='disease',
            name='prescriptions',
        ),
        migrations.RemoveField(
            model_name='patient',
            name='prescription',
        ),
        migrations.AddField(
            model_name='medicineintake',
            name='disease',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='patient.disease'),
        ),
        migrations.AddField(
            model_name='medicineintake',
            name='patient',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='patient.patient'),
        ),
        migrations.AlterField(
            model_name='medicineintake',
            name='quantity',
            field=models.CharField(choices=[('3', 'Three Time'), ('1', 'One Time'), ('2', 'Two Time')], max_length=5),
        ),
    ]