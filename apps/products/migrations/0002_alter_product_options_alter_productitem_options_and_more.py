# Generated by Django 4.1.6 on 2023-03-02 08:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('categories', '0002_alter_category_options_alter_category_parent_and_more'),
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='product',
            options={'verbose_name_plural': 'Товары'},
        ),
        migrations.AlterModelOptions(
            name='productitem',
            options={'verbose_name_plural': 'Данные товара'},
        ),
        migrations.AlterModelOptions(
            name='productitemimage',
            options={'verbose_name_plural': 'Изображение товара'},
        ),
        migrations.AlterField(
            model_name='product',
            name='categories',
            field=models.ManyToManyField(related_name='products', to='categories.category', verbose_name='категории'),
        ),
        migrations.AlterField(
            model_name='product',
            name='description',
            field=models.TextField(verbose_name='описание'),
        ),
        migrations.AlterField(
            model_name='product',
            name='name',
            field=models.CharField(db_index=True, max_length=255, verbose_name='наименование товара'),
        ),
        migrations.AlterField(
            model_name='productitem',
            name='color',
            field=models.CharField(choices=[('BLACK', 'Black'), ('BLUE', 'Blue'), ('RED', 'Red'), ('BROWN', 'Brown'), ('PURPLE', 'Purple')], db_index=True, max_length=255, verbose_name='цвет'),
        ),
        migrations.AlterField(
            model_name='productitem',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=10, verbose_name='цена'),
        ),
        migrations.AlterField(
            model_name='productitem',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product_items', to='products.product', verbose_name='продукт'),
        ),
        migrations.AlterField(
            model_name='productitem',
            name='quantity',
            field=models.PositiveIntegerField(verbose_name='количество'),
        ),
        migrations.AlterField(
            model_name='productitem',
            name='size',
            field=models.CharField(max_length=20, verbose_name='размер'),
        ),
        migrations.AlterField(
            model_name='productitemimage',
            name='image',
            field=models.ImageField(upload_to='productImages', verbose_name='изображение'),
        ),
        migrations.AlterField(
            model_name='productitemimage',
            name='product_item',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product_item_images', to='products.productitem', verbose_name='Позиция товара'),
        ),
    ]
