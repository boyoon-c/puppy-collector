# Generated by Django 3.2.6 on 2021-09-02 04:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0004_toy'),
    ]

    operations = [
        migrations.AddField(
            model_name='puppy',
            name='toys',
            field=models.ManyToManyField(to='main_app.Toy'),
        ),
    ]
