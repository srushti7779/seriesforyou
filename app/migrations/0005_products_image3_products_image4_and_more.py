# Generated by Django 4.1.7 on 2023-04-03 11:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_rename_image1_products_imagebw1_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='image3',
            field=models.ImageField(default='1.jpg', upload_to='productImage'),
        ),
        migrations.AddField(
            model_name='products',
            name='image4',
            field=models.ImageField(default='1.jpg', upload_to='productImage'),
        ),
        migrations.AlterField(
            model_name='products',
            name='imagebw1',
            field=models.ImageField(default='1.jpg', upload_to='productImage'),
        ),
        migrations.AlterField(
            model_name='products',
            name='imageclr2',
            field=models.ImageField(default='1.jpg', upload_to='productImage'),
        ),
    ]
