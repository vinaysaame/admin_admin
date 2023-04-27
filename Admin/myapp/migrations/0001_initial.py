# Generated by Django 4.1.6 on 2023-04-24 06:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AnimalCampModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Organisername', models.CharField(max_length=100)),
                ('category', models.CharField(choices=[('1', 'for dogs'), ('2', ' for Goats and sheeps'), ('3,', 'for cattles '), ('4', 'for birds'), ('4', 'for dogs,for Goats and sheeps,for cattles '), ('4', 'for all')], max_length=100)),
                ('place', models.CharField(max_length=100)),
                ('city', models.CharField(max_length=100)),
                ('camp_starts_at', models.CharField(max_length=100)),
                ('camp_ends_at', models.CharField(max_length=100)),
                ('date', models.DateField()),
                ('contact', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='ApplicantsModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=100)),
                ('contact', models.CharField(max_length=100)),
                ('city', models.CharField(max_length=100)),
                ('state', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Bloodcamp_event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Organisername', models.CharField(max_length=100)),
                ('place', models.CharField(max_length=100)),
                ('city', models.CharField(max_length=100)),
                ('camp_starts_at', models.CharField(max_length=100)),
                ('camp_ends_at', models.CharField(max_length=100)),
                ('date', models.DateField()),
                ('contact', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='CBEmodel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Organisername', models.CharField(max_length=100)),
                ('category', models.CharField(choices=[('1', 'festivals'), ('2', 'fairs'), ('3,', 'cultural celebrations ')], max_length=50)),
                ('topic', models.CharField(max_length=100)),
                ('place', models.CharField(max_length=100)),
                ('city', models.CharField(max_length=100)),
                ('camp_starts_at', models.CharField(max_length=100)),
                ('camp_ends_at', models.CharField(max_length=100)),
                ('date', models.DateField()),
                ('contact', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Educational_event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Organisername', models.CharField(max_length=100)),
                ('category', models.CharField(choices=[('1', 'workshops'), ('2', 'training sessions'), ('3,', 'classes '), ('4', 'job_mela')], max_length=50)),
                ('Topic', models.CharField(max_length=100)),
                ('eligibility', models.CharField(max_length=100)),
                ('place', models.CharField(max_length=100)),
                ('city', models.CharField(max_length=100)),
                ('camp_starts_at', models.CharField(max_length=100)),
                ('camp_ends_at', models.CharField(max_length=100)),
                ('date', models.DateField()),
                ('contact', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='ForScribersModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Scribename', models.CharField(max_length=100)),
                ('purpose', models.CharField(max_length=100)),
                ('place', models.CharField(max_length=100)),
                ('city', models.CharField(max_length=100)),
                ('camp_starts_at', models.TimeField()),
                ('camp_ends_at', models.TimeField()),
                ('date', models.DateField()),
                ('contact', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='MedicalCamp_event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Organiser_name', models.CharField(max_length=100)),
                ('place', models.CharField(max_length=100)),
                ('city', models.CharField(max_length=100)),
                ('camp_starts_at', models.CharField(max_length=100)),
                ('camp_ends_at', models.CharField(max_length=100)),
                ('Date', models.DateField()),
                ('contact_no', models.CharField(max_length=100)),
                ('For_whom', models.CharField(choices=[('Children', 'Children'), ('middle age', 'middle age'), ('old age', 'old age'), ('4', 'all')], max_length=100)),
                ('facilities', models.CharField(max_length=500)),
                ('message', models.CharField(max_length=100)),
            ],
        ),
    ]
