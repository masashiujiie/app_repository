# Generated by Django 4.1 on 2024-01-19 14:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('flick_seeker', '0002_reviewreaction_favoritemovie'),
    ]

    operations = [
        migrations.CreateModel(
            name='Favorite',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('movie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='flick_seeker.movie')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='flick_seeker.user')),
            ],
            options={
                'unique_together': {('user', 'movie')},
            },
        ),
    ]
