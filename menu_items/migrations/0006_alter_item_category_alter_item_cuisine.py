# Generated by Django 4.0.2 on 2022-03-17 14:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('menu_items', '0005_alter_item_category_alter_item_cuisine'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='category_label', to='menu_items.category'),
        ),
        migrations.AlterField(
            model_name='item',
            name='cuisine',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='cuisine_label', to='menu_items.cuisine'),
        ),
    ]
