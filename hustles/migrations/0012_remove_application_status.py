# Generated by Django 4.2.5 on 2024-12-06 10:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hustles', '0011_alter_application_status'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='application',
            name='status',
        ),
    ]
