# Generated by Django 2.2 on 2021-03-25 13:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('complaint', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='complaint',
            name='image',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
    ]
