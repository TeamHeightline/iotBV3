# Generated by Django 3.1.7 on 2021-03-08 06:36

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='QuestionThemes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250, verbose_name='Тема вопроса')),
                ('description', models.TextField(verbose_name='Описание')),
                ('created_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='Пользователь, который создал эту тему')),
            ],
            options={
                'verbose_name': 'Тема',
                'verbose_name_plural': 'Темы',
            },
        ),
        migrations.CreateModel(
            name='QuestionAuthor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250, verbose_name='Автор вопроса')),
                ('created_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='Пользователь, который создал этого автора')),
            ],
            options={
                'verbose_name': 'Автор вопроса',
                'verbose_name_plural': 'Авторы вопросов',
            },
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(verbose_name='Текст вопроса')),
                ('video_url', models.URLField(verbose_name='Ссылка на ютуб видео с вопросом')),
                ('author', models.ManyToManyField(related_name='question_authors', to='usertests.QuestionAuthor', verbose_name='Автор вопроса')),
                ('created_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='Пользователь, который создал этот вопрос')),
                ('theme', models.ManyToManyField(related_name='question_themes', to='usertests.QuestionThemes', verbose_name='Темы вопроса')),
            ],
            options={
                'verbose_name': 'Вопрос',
                'verbose_name_plural': 'Вопросы',
            },
        ),
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_true', models.BooleanField(default=True, verbose_name='Ответ правильный/ошибочный')),
                ('text', models.TextField(default='', verbose_name='Формулировка ответа')),
                ('help_textV1', models.TextField(default='', verbose_name='Подсказка для упрощенного уровня')),
                ('help_textV2', models.TextField(default='', verbose_name='Подсказка для нормального уровня')),
                ('help_textV3', models.TextField(default='', verbose_name='Подсказка для усложненного уровня')),
                ('video_url', models.URLField(verbose_name='Ссылка на ютуб видео с ответом')),
                ('check_queue', models.PositiveIntegerField(default=0, verbose_name='Очередь проверки, чем меньше - тем раньше вопрос будет проверен')),
                ('hard_level_of_answer', models.CharField(choices=[('EASY', 'Очевидный'), ('MEDIUM', 'Обычный'), ('HARD', 'Каверзный')], default='MEDIUM', max_length=10)),
                ('created_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='Пользователь, который создал этот ответ')),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='answers', to='usertests.question')),
            ],
            options={
                'verbose_name': 'Ответ',
                'verbose_name_plural': 'Ответы',
            },
        ),
    ]