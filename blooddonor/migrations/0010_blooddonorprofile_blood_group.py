# Generated by Django 2.1.7 on 2019-08-03 17:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blooddonor', '0009_blooddonorprofile_profile_picture'),
    ]

    operations = [
        migrations.AddField(
            model_name='blooddonorprofile',
            name='blood_group',
            field=models.CharField(choices=[('A+', 'A+'), ('A-', 'A-'), ('B+', 'B+'), ('B-', 'B-'), ('AB+', 'AB+'), ('AB-', 'AB-'), ('O+', 'O+'), ('O-', 'O-')], max_length=3, null=True),
        ),
    ]
