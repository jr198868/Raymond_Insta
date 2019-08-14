# Generated by Django 2.2.3 on 2019-08-01 22:33

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Insta', '0003_userconnection'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='posted_on',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name='userconnection',
            name='following',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='followings', to=settings.AUTH_USER_MODEL),
        ),
    ]