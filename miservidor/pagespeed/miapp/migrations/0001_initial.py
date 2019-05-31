# Generated by Django 2.2.1 on 2019-05-31 08:32

from django.db import migrations, models
import djongo.models.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dominio', models.CharField(max_length=255)),
                ('porcentaje_movil', models.CharField(max_length=255)),
                ('orportunidades_movil', djongo.models.fields.ListField()),
                ('diagnosticos_movil', djongo.models.fields.ListField()),
                ('porcentaje_ordenador', models.CharField(max_length=255)),
                ('oportunidades_ordenador', djongo.models.fields.ListField()),
                ('diagnosticos_ordenador', djongo.models.fields.ListField()),
            ],
        ),
    ]
