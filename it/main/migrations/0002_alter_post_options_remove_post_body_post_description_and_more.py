# Generated by Django 4.2.8 on 2024-07-01 18:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ['-publish'], 'verbose_name': 'Пост', 'verbose_name_plural': 'Посты'},
        ),
        migrations.RemoveField(
            model_name='post',
            name='body',
        ),
        migrations.AddField(
            model_name='post',
            name='description',
            field=models.TextField(max_length=500, null=True, verbose_name='Краткое описание'),
        ),
        migrations.AddField(
            model_name='post',
            name='text',
            field=models.TextField(null=True, verbose_name='Полный текст записи'),
        ),
    ]
