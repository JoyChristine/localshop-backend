# Generated by Django 4.0.5 on 2022-07-05 11:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('localapp', '0005_remove_order_clerk'),
    ]

    operations = [
        migrations.AddField(
            model_name='defectivegood',
            name='category',
            field=models.CharField(choices=[('1', 'electronics'), ('2', 'foods'), ('3', 'detergents'), ('4', 'kitchen-ware'), ('5', 'toys')], max_length=20, null=True),
        ),
    ]
