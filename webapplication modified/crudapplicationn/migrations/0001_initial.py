# Generated by Django 3.0.7 on 2020-08-22 06:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('roll_no', models.CharField(max_length=20)),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('contact', models.CharField(max_length=15)),
                ('father_name', models.CharField(max_length=20)),
                ('occupation', models.CharField(max_length=20)),
                ('address', models.CharField(max_length=200)),
                ('ia1_th', models.IntegerField(max_length=5)),
                ('ia1_pr', models.IntegerField(max_length=5)),
                ('ia1_att', models.IntegerField()),
                ('ia2_th', models.IntegerField(max_length=5)),
                ('ia2_pr', models.IntegerField(max_length=5)),
                ('ia2_att', models.IntegerField()),
                ('ia3_th', models.IntegerField(max_length=5)),
                ('ia3_pr', models.IntegerField(max_length=5)),
                ('ia3_att', models.IntegerField()),
                ('university_exam', models.IntegerField(max_length=5)),
            ],
        ),
    ]
