# Generated by Django 3.1.2 on 2020-10-08 20:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0007_remove_song_books'),
    ]

    operations = [
        migrations.AddField(
            model_name='song',
            name='books',
            field=models.ManyToManyField(to='main_app.Book'),
        ),
    ]
