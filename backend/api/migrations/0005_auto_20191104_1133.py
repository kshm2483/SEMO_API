# Generated by Django 2.2.4 on 2019-11-04 11:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_auto_20191104_1039'),
    ]

    operations = [
        migrations.AddField(
            model_name='endpoints',
            name='method',
            field=models.CharField(default=1, max_length=30),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='endpoints',
            name='name',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
    ]
