# Generated by Django 4.0.2 on 2022-02-24 20:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu_items', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name_plural': 'Categories'},
        ),
        migrations.AddField(
            model_name='item',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
    ]
