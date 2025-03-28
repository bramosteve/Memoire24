# Generated by Django 5.1.5 on 2025-02-06 07:54

import shortuuid.main
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chatapp', '0017_alter_chatgroup_group_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='groupmessage',
            name='encrypted_body',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='chatgroup',
            name='group_name',
            field=models.CharField(default=shortuuid.main.ShortUUID.uuid, max_length=128, unique=True),
        ),
    ]
