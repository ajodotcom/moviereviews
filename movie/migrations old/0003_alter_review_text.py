# Generated by Django 4.1.7 on 2023-03-20 09:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0002_review'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='text',
            field=models.CharField(max_length=101),
        ),
    ]
