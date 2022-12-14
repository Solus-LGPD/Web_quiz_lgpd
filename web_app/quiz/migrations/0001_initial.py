# Generated by Django 4.0.6 on 2022-09-26 20:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cadastro',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_empresa', models.CharField(max_length=100)),
                ('nome_colaborador', models.CharField(max_length=100)),
                ('email_colaborador', models.EmailField(max_length=100, unique=True)),
                ('whatsapp_colaborador', models.CharField(max_length=25, unique=True)),
                ('senha', models.CharField(max_length=30)),
                ('termo_de_uso', models.BooleanField(default=False, verbose_name='Eu aceito os termos de uso')),
            ],
        ),
        migrations.CreateModel(
            name='OpcaoResposta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('respostas', models.CharField(max_length=200, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Pergunta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pergunta', models.CharField(max_length=300, unique=True)),
                ('pesos', models.FloatField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Questao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('resposta', models.CharField(default=None, max_length=1, null=True)),
                ('data_de_envio', models.DateTimeField(blank=True, null=True, verbose_name='data de envio')),
                ('empresa', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='quiz.cadastro')),
                ('opcao_resposta', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='quiz.opcaoresposta')),
                ('pergunta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='quiz.pergunta')),
            ],
        ),
    ]
