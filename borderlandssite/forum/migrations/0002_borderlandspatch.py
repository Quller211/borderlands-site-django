# Generated by Django 4.1.2 on 2022-10-25 19:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='borderlandspatch',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('cat', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='forum.category')),
            ],
        ),
    ]
