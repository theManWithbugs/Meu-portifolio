# Generated by Django 5.1.1 on 2024-09-22 18:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_comment'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Comment',
            new_name='Profile',
        ),
        migrations.RenameField(
            model_name='profile',
            old_name='user_coments',
            new_name='text_profile',
        ),
        migrations.AlterField(
            model_name='nomeuser',
            name='cpf',
            field=models.CharField(max_length=11, primary_key=True, serialize=False, unique=True, verbose_name='Digite o CPF:'),
        ),
        migrations.AlterField(
            model_name='nomeuser',
            name='nome',
            field=models.CharField(max_length=80, verbose_name='Nome Completo:'),
        ),
        migrations.AlterField(
            model_name='nomeuser',
            name='sobrenome',
            field=models.CharField(max_length=80, verbose_name='Sobrenome:'),
        ),
    ]
