# Generated by Django 4.2.5 on 2023-09-06 17:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_campaign'),
    ]

    operations = [
        migrations.RenameField(
            model_name='subscriber',
            old_name='subsriber_id',
            new_name='subscriber_id',
        ),
    ]
