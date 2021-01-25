# Generated by Django 3.1.5 on 2021-01-25 09:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fname', models.CharField(max_length=50)),
                ('lname', models.CharField(max_length=50)),
                ('phone', models.IntegerField(default=0)),
                ('email', models.EmailField(max_length=500)),
                ('password', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Item_data',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('key', models.IntegerField()),
                ('customer', models.CharField(max_length=100)),
                ('item_name', models.CharField(max_length=100)),
                ('item_quantity', models.CharField(max_length=100)),
                ('item_status', models.CharField(max_length=100)),
                ('date', models.DateField()),
            ],
        ),
    ]
