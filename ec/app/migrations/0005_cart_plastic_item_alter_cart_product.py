# Generated by Django 5.0.6 on 2024-09-11 09:26

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_cart'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='plastic_item',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app.plasticitem'),
        ),
        migrations.AlterField(
            model_name='cart',
            name='product',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app.product'),
        ),
    ]
