# Generated by Django 3.2.8 on 2021-10-13 04:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_rename_localidae_clientes_localidade'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clientes',
            name='cep',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='clientes',
            name='cpf',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='clientes',
            name='email',
            field=models.EmailField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='clientes',
            name='telefone',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
