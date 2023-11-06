# Generated by Django 4.2.4 on 2023-08-29 16:42

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('rooms', '0004_remove_rooms_capacity'),
    ]

    operations = [
        migrations.CreateModel(
            name='MyRoom',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rooms', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='my_rooms', to='rooms.rooms')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='my_profile', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
