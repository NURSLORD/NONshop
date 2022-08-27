# Generated by Django 3.2 on 2022-07-02 10:25

from django.db import migrations, models
import django.db.models.deletion
import smart_selects.db_fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('customers', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=80, unique=True, verbose_name='Название')),
                ('description', models.TextField(verbose_name='О категория')),
                ('is_active', models.BooleanField(default=True, verbose_name='Подтверждённый')),
                ('image', models.ImageField(upload_to='Category/%Y/%m/%d', verbose_name='Фото')),
            ],
            options={
                'verbose_name': 'Категория',
                'verbose_name_plural': 'Категории',
            },
        ),
        migrations.CreateModel(
            name='SubCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=80, verbose_name='Название')),
                ('is_active', models.BooleanField(default=True, verbose_name='Подтверждённый')),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='product.category', verbose_name='Категория')),
            ],
            options={
                'verbose_name': 'Под-категория',
                'verbose_name_plural': 'Под-категории',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=80, verbose_name='Название')),
                ('image', models.ImageField(upload_to='Product/%Y/%m/%d', verbose_name='Фото')),
                ('description', models.TextField(verbose_name='Описание')),
                ('gender', models.CharField(blank=True, choices=[('M', 'Мужской'), ('W', 'Женский')], max_length=1, null=True, verbose_name='Пол')),
                ('is_popular', models.BooleanField(default=True, null=True, verbose_name='Популярный?')),
                ('amount', models.PositiveIntegerField(default=1, verbose_name='Кол-во')),
                ('article', models.BigIntegerField(null=True, unique=True, verbose_name='Артикл')),
                ('old_price', models.PositiveIntegerField(default=0, verbose_name='Старая цена')),
                ('cur', models.CharField(choices=[('COM', 'сом'), ('USD', 'доллар'), ('RUB', 'руб')], default='C', max_length=3, verbose_name='Волюта')),
                ('new_price', models.IntegerField(blank=True, null=True, verbose_name='Новая цена')),
                ('pub_date', models.DateField(auto_now_add=True, null=True, verbose_name='Дата публикации')),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='product.category', verbose_name='Категория')),
                ('sub_category', smart_selects.db_fields.ChainedForeignKey(auto_choose=True, chained_field='category', chained_model_field='category', on_delete=django.db.models.deletion.CASCADE, to='product.subcategory', verbose_name='Под-категория')),
            ],
            options={
                'verbose_name': 'Продукт',
                'verbose_name_plural': 'Продукты',
            },
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fee', models.CharField(choices=[('CASH', 'Наличка'), ('CARD', 'Карта')], default='CARD', max_length=4, verbose_name='Платеж')),
                ('service', models.BooleanField(default=True, verbose_name='Доставка')),
                ('address', models.CharField(max_length=80, verbose_name='Адрес')),
                ('total_item', models.PositiveIntegerField(default=1, verbose_name='Кол-во')),
                ('ord_date', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Дата заказа')),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='customers.customer', verbose_name='Клиент')),
            ],
            options={
                'verbose_name': 'Заказчик',
                'verbose_name_plural': 'Заказчики',
            },
        ),
        migrations.CreateModel(
            name='ItemOrders',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(default=1, verbose_name='Кол-во')),
                ('color', models.CharField(max_length=20, verbose_name='Цвет')),
                ('order', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='product.order', verbose_name='Заказчик')),
                ('product', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='product.product', verbose_name='Продукт')),
            ],
            options={
                'verbose_name': 'Заказ',
                'verbose_name_plural': 'Заказы',
            },
        ),
    ]
