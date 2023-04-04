# Generated by Django 4.1.7 on 2023-04-04 13:17

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wallet_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='wallet',
            name='wallet_user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='user', to=settings.AUTH_USER_MODEL),
        ),
    ]