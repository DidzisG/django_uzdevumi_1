# Generated by Django 3.2.9 on 2021-11-22 19:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('uzdevumi', '0002_auto_20211122_1855'),
    ]

    operations = [
        migrations.RenameField(
            model_name='visit',
            old_name='visitor',
            new_name='user',
        ),
    ]