# Generated by Django 5.0.6 on 2024-05-30 13:19

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs_app', '0002_remove_blogimages_image_ppoi_remove_blogimages_name_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='ImageFiles',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(upload_to='blog_images/')),
            ],
        ),
        migrations.RemoveField(
            model_name='image',
            name='image',
        ),
        migrations.RemoveField(
            model_name='blog',
            name='image',
        ),
        migrations.RemoveField(
            model_name='image',
            name='author',
        ),
        migrations.CreateModel(
            name='PostImages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='img', to='blogs_app.imagefiles')),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='blogs_app.blog')),
            ],
        ),
        migrations.DeleteModel(
            name='BlogImages',
        ),
        migrations.DeleteModel(
            name='Image',
        ),
    ]
