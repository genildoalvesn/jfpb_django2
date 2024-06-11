# Generated by Django 3.2.25 on 2024-06-11 12:07

import cadastros.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cadastros', '0002_alter_campo_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Classe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50, verbose_name='classe')),
                ('descricao', models.CharField(blank=True, max_length=150, null=True, verbose_name='Descrição')),
                ('nivel', models.IntegerField(verbose_name='nivel')),
            ],
        ),
        migrations.CreateModel(
            name='Progressao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('servidor', models.CharField(max_length=255)),
                ('classe', models.CharField(max_length=255)),
                ('data_inicial', models.DateField()),
                ('data_final', models.DateField(blank=True, null=True)),
                ('observacao', models.CharField(max_length=255, verbose_name='Observação')),
            ],
        ),
        migrations.CreateModel(
            name='Comprovante',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantidade', models.DecimalField(decimal_places=2, max_digits=5)),
                ('data', models.DateField()),
                ('data_final', models.DateField(blank=True, help_text='informe apenas se o comprovante for relativo a um periodo.', null=True)),
                ('arquivo', models.FileField(upload_to=cadastros.models.user_path)),
                ('atividade', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='cadastros.atividade')),
                ('progresso', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='cadastros.progressao', verbose_name='progressao')),
            ],
        ),
    ]
