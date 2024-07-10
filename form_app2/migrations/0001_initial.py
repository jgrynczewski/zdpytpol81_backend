# Generated by Django 5.0.6 on 2024-07-10 16:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('category', models.CharField(choices=[('question', 'Pytanie'), ('other', 'Inne')], max_length=100)),
                ('subject', models.CharField(max_length=100)),
                ('body', models.TextField()),
                ('date', models.DateField()),
                ('time', models.TimeField()),
                ('added', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateField(auto_now=True)),
            ],
        ),
    ]
