# Generated by Django 3.2.5 on 2021-08-02 11:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('graphql_api', '0002_post'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='create_by',
            new_name='created_by',
        ),
        migrations.AlterField(
            model_name='user',
            name='name',
            field=models.CharField(max_length=250),
        ),
    ]
