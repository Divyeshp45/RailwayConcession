# Generated by Django 4.1.1 on 2022-10-15 16:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ContactU',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=150)),
                ('mobile_1', models.IntegerField()),
                ('mobile_2', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='StudentApplication',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=20)),
                ('last_name', models.CharField(max_length=20)),
                ('app_type', models.CharField(max_length=20)),
                ('tenure', models.CharField(max_length=20)),
                ('reg_id', models.CharField(max_length=10)),
                ('email_id', models.EmailField(max_length=30)),
                ('aadhar_no', models.CharField(max_length=20)),
                ('address', models.TextField(max_length=200)),
                ('station', models.CharField(max_length=20)),
                ('junction', models.CharField(max_length=20)),
                ('date', models.CharField(max_length=10)),
            ],
        ),
    ]