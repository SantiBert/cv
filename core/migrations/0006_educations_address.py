# Generated by Django 3.2.9 on 2021-11-05 04:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_maincontent_cv'),
    ]

    operations = [
        migrations.AddField(
            model_name='educations',
            name='address',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
    ]
