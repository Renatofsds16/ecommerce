# Generated by Django 4.2.5 on 2023-09-13 00:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('short_description', models.TextField(max_length=125)),
                ('long_description', models.TextField(max_length=255)),
                ('image', models.ImageField(upload_to='%Y/%m')),
                ('slug', models.SlugField(unique=True)),
                ('price_marketing', models.FloatField()),
                ('price_marketing_promotional', models.FloatField(default=0)),
                ('types', models.CharField(choices=[('v', 'variaçao'), ('s', 'simples')], default='v', max_length=1)),
            ],
            options={
                'verbose_name': 'produto',
                'verbose_name_plural': 'produtos',
            },
        ),
        migrations.CreateModel(
            name='Variation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=125)),
                ('price', models.FloatField()),
                ('price_promotional', models.FloatField(default=0)),
                ('stock', models.PositiveIntegerField(default=1)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='produto.product')),
            ],
            options={
                'verbose_name': 'variacao',
                'verbose_name_plural': 'variaçoes',
            },
        ),
    ]
