# Generated by Django 4.0.5 on 2022-06-23 05:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('salescall', '0003_add_comment_model'),
    ]

    operations = [
        migrations.AddField(
            model_name='callrecord',
            name='is_draft',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='callrecord',
            name='is_open',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='historicalcallrecord',
            name='is_draft',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='historicalcallrecord',
            name='is_open',
            field=models.BooleanField(default=True),
        ),
    ]
