# Generated by Django 5.0.6 on 2024-07-02 11:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0004_categoria"),
    ]

    operations = [
        migrations.AlterField(
            model_name="categoria",
            name="descricao",
            field=models.CharField(max_length=100),
        ),
    ]