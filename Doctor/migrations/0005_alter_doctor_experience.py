# Generated by Django 4.2 on 2024-05-06 11:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Doctor', '0004_doctor_user_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctor',
            name='experience',
            field=models.CharField(max_length=1000),
        ),
    ]
