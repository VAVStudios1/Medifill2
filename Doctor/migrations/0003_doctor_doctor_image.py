# Generated by Django 4.2 on 2024-03-30 13:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Doctor', '0002_appointment'),
    ]

    operations = [
        migrations.AddField(
            model_name='doctor',
            name='doctor_image',
            field=models.ImageField(default=True, upload_to=''),
        ),
    ]
