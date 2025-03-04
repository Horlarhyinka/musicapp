# Generated by Django 5.0.6 on 2024-05-28 00:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='music',
            name='cover',
            field=models.URLField(default='https://wikisound.org/mastering/Audio-waveform-player/data/default_artwork/music_ph.png'),
        ),
        migrations.AlterField(
            model_name='music',
            name='url',
            field=models.URLField(default='https://www.soundhelix.com/examples/mp3/SoundHelix-Song-1.mp3'),
        ),
    ]
