# Generated by Django 4.2 on 2024-04-15 14:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Product', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product_variant',
            old_name='size_medi',
            new_name='size_medi_mg',
        ),
    ]
