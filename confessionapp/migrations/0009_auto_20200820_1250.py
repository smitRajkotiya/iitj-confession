# Generated by Django 3.0.2 on 2020-08-20 07:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('confessionapp', '0008_auto_20200815_1009'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='conf',
            name='nooflikes',
        ),
        migrations.RemoveField(
            model_name='conf',
            name='noofloves',
        ),
        migrations.RemoveField(
            model_name='conf',
            name='noofsad',
        ),
        migrations.AlterField(
            model_name='conf',
            name='image',
            field=models.ImageField(null=True, upload_to='images/'),
        ),
        migrations.AlterField(
            model_name='conf',
            name='noofangrey',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='conf',
            name='noofhaha',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='conf',
            name='noofwows',
            field=models.IntegerField(),
        ),
    ]