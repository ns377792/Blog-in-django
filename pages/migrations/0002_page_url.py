# Generated by Django 2.2.12 on 2022-01-05 06:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='page',
            name='url',
            field=models.CharField(default='page', max_length=155),
            preserve_default=False,
        ),
    ]
