# Generated by Django 4.1.5 on 2023-01-13 16:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('feed', '0001_initial'),
        ('post', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='feed',
            name='posts',
            field=models.ManyToManyField(blank=True, to='post.post'),
        ),
    ]
