# Generated by Django 3.1.4 on 2020-12-25 12:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0007_remove_test_tel'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Test',
            new_name='User',
        ),
    ]