# Generated by Django 4.1.6 on 2023-03-02 08:21

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('products', '0002_alter_product_options_alter_productitem_options_and_more'),
        ('carts', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='cart',
            options={'verbose_name_plural': 'Корзина'},
        ),
        migrations.AlterModelOptions(
            name='cartitem',
            options={'verbose_name_plural': 'Товары в Корзине'},
        ),
        migrations.AlterField(
            model_name='cart',
            name='user',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Корзина'),
        ),
        migrations.AlterField(
            model_name='cartitem',
            name='amount',
            field=models.PositiveIntegerField(blank=True, default=1, verbose_name='количество'),
        ),
        migrations.AlterField(
            model_name='cartitem',
            name='cart',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cart_items', to='carts.cart', verbose_name='Корзина'),
        ),
        migrations.AlterField(
            model_name='cartitem',
            name='product_item',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product_in_cart', to='products.productitem', verbose_name='Позиция продукта'),
        ),
    ]