# Generated by Django 4.1.7 on 2023-02-21 14:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newspaper', '0002_alter_post_text'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='text',
            field=models.TextField(),
        ),
    ]
