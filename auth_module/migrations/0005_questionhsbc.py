# Generated by Django 5.0.3 on 2024-04-04 11:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auth_module', '0004_companyinfo'),
    ]

    operations = [
        migrations.CreateModel(
            name='QuestionHSBC',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('QId', models.CharField(max_length=25, unique=True)),
                ('Question', models.TextField(default=True)),
                ('Option1', models.TextField(default=True)),
                ('Option2', models.TextField(default=True)),
                ('Option3', models.TextField(default=True)),
                ('Option4', models.TextField(default=True)),
                ('Answer', models.TextField(default=True)),
                ('q_type', models.TextField(default=True)),
            ],
        ),
    ]