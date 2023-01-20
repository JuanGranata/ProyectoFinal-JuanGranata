# Generated by Django 4.1.3 on 2023-01-19 18:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppMessages', '0005_alter_msg_userto'),
    ]

    operations = [
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sender', models.CharField(max_length=200)),
                ('receiver', models.CharField(max_length=200)),
                ('subject', models.CharField(max_length=200, null=True)),
                ('content', models.CharField(blank=True, max_length=10000, null=True)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('seen', models.BooleanField(null=True)),
            ],
        ),
    ]