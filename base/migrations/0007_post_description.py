# Generated by Django 4.1.9 on 2023-12-03 02:27

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0006_post_cost'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='description',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
    ]
