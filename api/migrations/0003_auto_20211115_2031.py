# Generated by Django 3.2.8 on 2021-11-15 20:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20211016_1658'),
    ]

    operations = [
        migrations.RenameField(
            model_name='fields',
            old_name='area',
            new_name='area_ha',
        ),
        migrations.RenameField(
            model_name='fields',
            old_name='code',
            new_name='field_code',
        ),
        migrations.RenameField(
            model_name='fields',
            old_name='name',
            new_name='field_name',
        ),
        migrations.RenameField(
            model_name='seasons',
            old_name='end',
            new_name='season_end',
        ),
        migrations.RenameField(
            model_name='seasons',
            old_name='name',
            new_name='season_name',
        ),
        migrations.RenameField(
            model_name='seasons',
            old_name='start',
            new_name='season_start',
        ),
    ]
