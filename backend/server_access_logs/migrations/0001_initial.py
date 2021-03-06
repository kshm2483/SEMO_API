# Generated by Django 2.2.4 on 2019-10-22 14:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AccessLogsModel',
            fields=[
                ('sys_id', models.AutoField(primary_key=True, serialize=False)),
                ('user', models.CharField(blank=True, max_length=512, null=True)),
                ('session_key', models.CharField(blank=True, max_length=1024)),
                ('path', models.CharField(blank=True, max_length=1024)),
                ('method', models.CharField(blank=True, max_length=8)),
                ('data', models.TextField(blank=True, null=True)),
                ('ip_address', models.CharField(blank=True, max_length=45)),
                ('referrer', models.CharField(blank=True, max_length=512, null=True)),
                ('timestamp', models.DateTimeField(blank=True)),
            ],
            options={
                'db_table': 'access_logs',
            },
        ),
    ]
