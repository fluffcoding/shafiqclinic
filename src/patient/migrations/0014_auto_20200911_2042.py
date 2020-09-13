# Generated by Django 3.1 on 2020-09-11 20:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patient', '0013_auto_20200907_0504'),
    ]

    operations = [
        migrations.AlterField(
            model_name='medicineintake',
            name='medicine',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='medicineintake',
            name='quantity',
            field=models.CharField(choices=[('2', 'Two Time'), ('3', 'Three Time'), ('1', 'One Time')], max_length=5),
        ),
        migrations.DeleteModel(
            name='Medicine',
        ),
    ]
