# Generated by Django 3.1.7 on 2021-05-15 03:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_auto_20210513_1703'),
    ]

    operations = [
        migrations.RenameField(
            model_name='camisa',
            old_name='tela',
            new_name='Tela',
        ),
        migrations.RenameField(
            model_name='estampados',
            old_name='TCamisa',
            new_name='Camisa',
        ),
        migrations.RenameField(
            model_name='estampados',
            old_name='tela',
            new_name='Tela',
        ),
    ]
