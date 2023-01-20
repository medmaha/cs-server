# Generated by Django 4.1.5 on 2023-01-13 16:07

from django.db import migrations, models
import utilities.media_paths


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField(max_length=1000)),
                ('file', models.FileField(blank=True, null=True, upload_to=utilities.media_paths.comment_file_path)),
                ('picture', models.ImageField(blank=True, null=True, upload_to=utilities.media_paths.comment_picture_path)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('is_updated', models.BooleanField(default=False)),
                ('activity_rate', models.BigIntegerField(blank=True, default=1, null=True)),
            ],
            options={
                'ordering': ('-created_at', 'activity_rate', '-updated_at'),
            },
        ),
    ]
