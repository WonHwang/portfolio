# Generated by Django 3.0.8 on 2020-07-26 11:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_project_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='detail',
            field=models.TextField(null=True),
        ),
    ]