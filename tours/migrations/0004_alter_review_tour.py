# Generated by Django 4.1.3 on 2024-12-18 10:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tours', '0003_remove_order_tourist_order_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='tour',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reviews', to='tours.tour'),
        ),
    ]
