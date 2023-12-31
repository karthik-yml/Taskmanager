# Generated by Django 4.0 on 2023-08-06 10:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('tasklist', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tasks',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('due_date', models.DateField()),
                ('task_list', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tasklist.tasklist')),
            ],
        ),
    ]
