# Generated by Django 5.0.8 on 2024-08-29 09:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resumeApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='educationdetailsmodel',
            name='year',
            field=models.DateField(null=True),
        ),
    ]
