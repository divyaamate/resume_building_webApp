# Generated by Django 5.0.8 on 2024-10-01 14:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resumeApp', '0003_certificationmodel_experiancemodel_languagemodel_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='skillmodel',
            name='skill',
        ),
        migrations.AddField(
            model_name='skillmodel',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='skillmodel',
            name='name',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
