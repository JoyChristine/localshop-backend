# Generated by Django 4.0.5 on 2022-07-05 09:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Admin',
            fields=[
                ('name', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=20)),
                ('password', models.CharField(max_length=20)),
                ('AdminId', models.AutoField(primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Clerk',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=20)),
                ('password', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=20)),
                ('category', models.CharField(choices=[('1', 'electronics'), ('2', 'foods'), ('3', 'detergents'), ('4', 'kitchen-ware'), ('5', 'toys')], max_length=20, null=True)),
                ('quantity', models.IntegerField()),
                ('status', models.CharField(choices=[('1', 'Paid'), ('2', 'Unpaid')], max_length=20, null=True)),
                ('buying_price', models.IntegerField()),
                ('selling_price', models.IntegerField()),
                ('expiry_date', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(auto_now_add=True)),
                ('quantity', models.IntegerField()),
                ('clerk', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='localapp.clerk')),
                ('ordered_product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='localapp.product')),
            ],
        ),
        migrations.CreateModel(
            name='defectivegood',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('quantity', models.IntegerField()),
                ('clerk', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='localapp.clerk')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='localapp.product')),
            ],
        ),
    ]
