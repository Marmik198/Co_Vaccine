# Generated by Django 3.1.6 on 2021-05-03 16:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0013_appointment_center'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment',
            name='Address',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='appointment',
            name='City',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='appointment',
            name='Flatno',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='appointment',
            name='State',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='appointment',
            name='center',
            field=models.CharField(blank=True, max_length=500),
        ),
        migrations.AlterField(
            model_name='appointment',
            name='covid_status',
            field=models.CharField(default='Negative', max_length=500),
        ),
        migrations.AlterField(
            model_name='appointment',
            name='current_symptom',
            field=models.CharField(blank=True, default='N.A.', max_length=500),
        ),
        migrations.AlterField(
            model_name='appointment',
            name='dose',
            field=models.CharField(blank=True, max_length=500),
        ),
        migrations.AlterField(
            model_name='appointment',
            name='medical_issues',
            field=models.CharField(default='N.A.', max_length=500),
        ),
        migrations.AlterField(
            model_name='appointment',
            name='travel_history',
            field=models.CharField(default='No', max_length=500),
        ),
    ]