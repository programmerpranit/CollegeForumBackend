# Generated by Django 4.0.2 on 2022-03-15 19:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0002_answer_answer_text_question_image_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='question',
            name='image',
        ),
    ]
