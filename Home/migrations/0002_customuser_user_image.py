# Generated by Django 4.2 on 2024-04-01 09:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='User_image',
            field=models.ImageField(null=True, upload_to=''),
        ),
    ]
