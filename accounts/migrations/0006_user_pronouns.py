# Generated by Django 3.1.13 on 2021-09-20 00:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_remove_duplicate_perms'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='pronouns',
            field=models.CharField(blank=True, max_length=32, null=True, verbose_name='Pronouns'),
        ),
    ]
