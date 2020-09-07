# Generated by Django 3.1 on 2020-09-07 05:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patient', '0012_auto_20200907_0343'),
    ]

    operations = [
        migrations.AddField(
            model_name='patient',
            name='created',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name='medicineintake',
            name='quantity',
            field=models.CharField(choices=[('1', 'One Time'), ('2', 'Two Time'), ('3', 'Three Time')], max_length=5),
        ),
    ]