# Generated by Django 2.0.9 on 2020-02-13 15:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0003_auto_20200213_1534'),
    ]

    operations = [
        migrations.AlterField(
            model_name='baseprofile',
            name='picture',
            field=models.ImageField(blank=True, null=True, upload_to='profile_pics/%Y-%m-%d/', verbose_name='Profile picture'),
        ),
    ]