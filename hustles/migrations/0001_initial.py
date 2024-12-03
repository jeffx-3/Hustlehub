# Generated by Django 5.1.3 on 2024-12-03 18:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('emp_name', models.CharField(max_length=50)),
                ('emp_about', models.CharField(max_length=500)),
                ('emp_photo', models.ImageField(upload_to='media/')),
                ('emp_contact', models.CharField(max_length=35)),
                ('emp_skills', models.CharField(max_length=420)),
                ('emp_location', models.CharField(max_length=420)),
            ],
        ),
        migrations.CreateModel(
            name='employer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('boss_name', models.CharField(max_length=70)),
                ('boss_contact', models.CharField(max_length=70)),
                ('boss_location', models.CharField(max_length=45)),
            ],
        ),
        migrations.CreateModel(
            name='gig',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('rate', models.IntegerField()),
                ('description', models.CharField(max_length=420)),
                ('skill', models.CharField(max_length=120)),
                ('location', models.CharField(max_length=30)),
                ('date_posted', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
