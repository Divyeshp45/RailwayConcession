# Generated by Django 4.1.1 on 2022-10-15 18:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MyApp', '0002_alter_studentapplication_junction'),
    ]

    operations = [
        migrations.AddField(
            model_name='studentapplication',
            name='mobile',
            field=models.CharField(max_length=10, null=True, unique=True),
        ),
    ]
