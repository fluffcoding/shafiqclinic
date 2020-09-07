# Generated by Django 3.1 on 2020-08-17 13:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patient', '0008_auto_20200817_1316'),
    ]

    operations = [
        migrations.AlterField(
            model_name='medicineintake',
            name='quantity',
            field=models.CharField(choices=[('1', 'One Time'), ('2', 'Two Time'), ('3', 'Three Time')], max_length=5),
        ),
    ]
