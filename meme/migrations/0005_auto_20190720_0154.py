# Generated by Django 2.1.7 on 2019-07-19 23:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('meme', '0004_downvote_upvote'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='downvote',
            name='meme',
        ),
        migrations.RemoveField(
            model_name='downvote',
            name='user',
        ),
        migrations.RemoveField(
            model_name='upvote',
            name='meme',
        ),
        migrations.RemoveField(
            model_name='upvote',
            name='user',
        ),
        migrations.DeleteModel(
            name='Downvote',
        ),
        migrations.DeleteModel(
            name='Upvote',
        ),
    ]