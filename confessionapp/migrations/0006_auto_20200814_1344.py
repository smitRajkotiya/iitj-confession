# Generated by Django 3.0.2 on 2020-08-14 08:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('confessionapp', '0005_auto_20200814_1340'),
    ]

    operations = [
        migrations.RenameField(
            model_name='conf',
            old_name='img',
            new_name='image',
        ),
    ]
