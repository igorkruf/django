# Generated by Django 5.0 on 2024-01-28 17:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0006_rename_list_type_zapchast_type_product_listtypezapchasttypeproduct_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='typezapchast',
            name='name',
            field=models.IntegerField(),
        ),
    ]
