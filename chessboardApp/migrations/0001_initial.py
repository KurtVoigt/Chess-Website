# Generated by Django 3.0.9 on 2021-03-22 12:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Board',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('board_name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Space',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('space_col', models.CharField(max_length=1)),
                ('space_row', models.IntegerField()),
                ('space_piece', models.CharField(max_length=6)),
                ('board', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='chessboardApp.Board')),
            ],
        ),
    ]