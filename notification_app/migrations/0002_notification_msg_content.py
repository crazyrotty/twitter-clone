# Generated by Django 3.2.5 on 2021-08-04 01:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('notification_app', '0001_initial'),
        ('tweet_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='notification',
            name='msg_content',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tweet_app.tweet'),
        ),
    ]
