# Generated by Django 3.1.7 on 2021-03-16 04:35

from django.db import migrations, models
import django.db.models.deletion
import main_app.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contacts',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city', models.CharField(max_length=128, unique=True, verbose_name='Город')),
                ('address', models.CharField(max_length=256, verbose_name='Адрес')),
                ('phone', models.CharField(max_length=64, verbose_name='Телефон')),
                ('email', models.EmailField(max_length=254)),
            ],
            options={
                'verbose_name': 'Контакт',
                'verbose_name_plural': 'Контакты',
            },
        ),
        migrations.CreateModel(
            name='ProductCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, unique=True, verbose_name='Категория')),
                ('description', models.CharField(blank=True, max_length=128, verbose_name='Описание')),
                ('is_active', models.BooleanField(db_index=True, default=True, verbose_name='Активна')),
            ],
            options={
                'verbose_name': 'Категория',
                'verbose_name_plural': 'Категории',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, unique=True, verbose_name='Наименование продукта')),
                ('short_desc', models.CharField(blank=True, max_length=128, verbose_name='Краткое описание')),
                ('description', models.TextField(blank=True, verbose_name='Описание')),
                ('price', models.DecimalField(decimal_places=2, default=0, max_digits=8, verbose_name='Цена')),
                ('quantity', models.PositiveSmallIntegerField(default=0, verbose_name='Количество')),
                ('is_active', models.BooleanField(default=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.productcategory')),
            ],
            options={
                'verbose_name': 'Продукт',
                'verbose_name_plural': 'Продукты',
            },
        ),
        migrations.CreateModel(
            name='Images',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('upload', models.ImageField(upload_to=main_app.models.product_directory_path)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.product')),
            ],
            options={
                'verbose_name': 'Фотография продукта',
                'verbose_name_plural': 'Фотографии продуктов',
            },
        ),
    ]