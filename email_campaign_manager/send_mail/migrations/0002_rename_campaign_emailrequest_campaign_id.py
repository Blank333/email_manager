# Generated by Django 4.2.5 on 2023-09-07 16:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('send_mail', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='emailrequest',
            old_name='campaign',
            new_name='campaign_id',
        ),
    ]
