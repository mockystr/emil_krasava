# Generated by Django 2.0.5 on 2018-10-28 11:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_auto_20181015_0140'),
    ]

    operations = [
        migrations.CreateModel(
            name='Catalog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=200, verbose_name='Наименование')),
                ('slug', models.SlugField(max_length=200, unique=True)),
                ('file', models.FileField(upload_to='catalogs/%Y/%m', verbose_name='Файл')),
                ('image', models.ImageField(default='../static/image/not_found.jpg', upload_to='category/%Y/%m', verbose_name='Фотография категории')),
            ],
            options={
                'verbose_name': 'Каталог',
                'verbose_name_plural': 'Каталоги',
                'ordering': ('name',),
            },
        ),
    ]
