# Generated by Django 5.0.6 on 2024-07-08 15:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orm_app', '0003_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Task',
        ),
    ]