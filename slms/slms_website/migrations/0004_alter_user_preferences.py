# Generated by Django 5.0.6 on 2024-11-10 14:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('slms_website', '0003_user_preferences_delete_userpreferences'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='preferences',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]