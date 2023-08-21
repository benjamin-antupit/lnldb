# Generated by Django 3.1.8 on 2021-11-10 22:07

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('events', '0005_survey_default'),
    ]

    operations = [
        migrations.AlterField(
            model_name='baseevent',
            name='client_contact',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='client_contact', to=settings.AUTH_USER_MODEL, verbose_name='Client Contact'),
        ),
    ]
