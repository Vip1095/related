# Generated by Django 3.2.9 on 2022-05-09 16:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author_name', models.CharField(max_length=120)),
            ],
        ),
        migrations.CreateModel(
            name='Books',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('book_name', models.CharField(max_length=120)),
                ('helped_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='helped_author', to='Related_app.author')),
                ('written_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='authors', to='Related_app.author')),
            ],
        ),
    ]
