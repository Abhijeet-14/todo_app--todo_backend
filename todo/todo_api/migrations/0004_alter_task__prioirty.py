# Generated by Django 4.1.2 on 2022-10-08 19:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("todo_api", "0003_alter_task__prioirty"),
    ]

    operations = [
        migrations.AlterField(
            model_name="task",
            name="_prioirty",
            field=models.CharField(max_length=120),
        ),
    ]
