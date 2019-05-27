# Generated by Django 2.2 on 2019-05-27 05:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('face', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('subdivision', models.CharField(max_length=50)),
                ('reason', models.CharField(max_length=50)),
                ('where', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('price', models.FloatField()),
                ('quantity', models.FloatField()),
                ('measurement', models.CharField(choices=[('шт', 'шт'), ('кг', 'кг'), ('м', 'м'), ('кт', 'кт')], default='шт', max_length=2)),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='face.Order')),
            ],
        ),
        migrations.DeleteModel(
            name='Post',
        ),
        migrations.DeleteModel(
            name='Thread',
        ),
    ]
