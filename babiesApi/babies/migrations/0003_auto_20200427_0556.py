# Generated by Django 3.0.5 on 2020-04-27 05:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('babies', '0002_baby_parent'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='baby',
            name='age',
        ),
        migrations.AddField(
            model_name='baby',
            name='birth',
            field=models.DateField(default='2020-01-01'),
            preserve_default=False,
        ),
    ]
