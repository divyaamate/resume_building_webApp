# Generated by Django 5.0.8 on 2024-10-01 14:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resumeApp', '0004_remove_skillmodel_skill_skillmodel_description_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='skillmodel',
            name='description',
        ),
        migrations.RemoveField(
            model_name='skillmodel',
            name='name',
        ),
        migrations.AddField(
            model_name='skillmodel',
            name='skill',
            field=models.CharField(max_length=200, null=True),
        ),
    ]