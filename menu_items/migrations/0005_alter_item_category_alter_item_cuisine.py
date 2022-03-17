# Generated by Django 4.0.2 on 2022-03-17 13:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('menu_items', '0004_cuisine_alter_item_category_item_cuisine'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='category', to='menu_items.category'),
        ),
        migrations.AlterField(
            model_name='item',
            name='cuisine',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='cuisine', to='menu_items.cuisine'),
        ),
    ]