# Generated by Django 3.2 on 2022-07-07 09:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='subcategory',
            name='image',
            field=models.ImageField(null=True, upload_to='Sub/%Y/%m/%d', verbose_name='Фото'),
        ),
    ]
