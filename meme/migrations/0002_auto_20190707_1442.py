# Generated by Django 2.1.7 on 2019-07-07 12:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('meme', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='meme',
            name='category',
            field=models.CharField(choices=[('LOL', 'LOL'), ('TFT', 'TFT'), ('SEX', 'SEX')], max_length=10),
        ),
    ]