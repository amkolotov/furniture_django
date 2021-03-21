# Generated by Django 3.1.7 on 2021-03-21 09:41

from django.db import migrations
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('auth_app', '0003_auto_20210317_0845'),
    ]

    operations = [
        migrations.AddField(
            model_name='shopuserprofile',
            name='phone',
            field=phonenumber_field.modelfields.PhoneNumberField(blank=True, error_messages={'invalid': 'Введите номер по образцу: +79120000000'}, max_length=128, region=None, verbose_name='Номер телефона'),
        ),
    ]