# Generated by Django 4.2.3 on 2023-07-29 14:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="data",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("user_id", models.IntegerField()),
                ("mov1", models.IntegerField()),
                ("mov2", models.IntegerField()),
                ("mov3", models.IntegerField()),
                ("mov4", models.IntegerField()),
                ("mov5", models.IntegerField()),
                ("totalWatchTime", models.FloatField()),
                ("weeklyWatchTime", models.FloatField()),
                ("rewardPoints", models.IntegerField()),
            ],
        ),
    ]
