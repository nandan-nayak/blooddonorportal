# Generated by Django 2.1.7 on 2019-08-03 17:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blooddonor', '0008_blooddonorprofile_qrcode'),
    ]

    operations = [
        migrations.AddField(
            model_name='blooddonorprofile',
            name='profile_picture',
            field=models.ImageField(null=True, upload_to='profiles/'),
        ),
    ]
