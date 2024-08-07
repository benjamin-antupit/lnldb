# Generated by Django 3.1.8 on 2021-04-30 04:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SlackMessage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('posted_to', models.CharField(max_length=128)),
                ('posted_by', models.CharField(max_length=24)),
                ('content', models.TextField()),
                ('blocks', models.BooleanField(default=False)),
                ('ts', models.CharField(max_length=24, verbose_name='Timestamp')),
                ('public', models.BooleanField(default=True)),
                ('deleted', models.BooleanField(default=False, help_text='Remove from the Slack workspace? This action cannot be undone.', verbose_name='Remove from workspace')),
                ('parent', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='slack.slackmessage')),
            ],
            options={
                'permissions': (('post_officer', 'Post Slack message as an officer'), ('post_official', 'Post Slack message as LNL'), ('manage_channel', 'Add or remove users from a Slack channel')),
            },
        ),
    ]
