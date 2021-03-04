from django.db import models
from django.contrib.postgres.fields import ArrayField
from django.contrib.auth.models import User


# Create your models here.


class QuestionThemes(models.Model):
    """Темы вопросов"""
    name = models.CharField("Тема вопроса", max_length=250)
    description = models.TextField("Описание")
    created_by = models.ForeignKey(User, verbose_name="Пользователь, который создал эту тему",
                                   on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Тема"
        verbose_name_plural = "Темы"


class QuestionAuthor(models.Model):
    """Автор вопроса"""
    name = models.CharField("Автор вопроса", max_length=250)
    created_by = models.ForeignKey(User, verbose_name="Пользователь, который создал этого автора",
                                   on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Автор вопроса"
        verbose_name_plural = "Авторы вопросов"


class Question(models.Model):
    created_by = models.ForeignKey(User, verbose_name="Пользователь, который создал этот вопрос",
                                   on_delete=models.SET_NULL, null=True)
    theme = models.ManyToManyField(QuestionThemes, verbose_name="Темы вопроса",
                                   related_name="question_themes")
    author = models.ManyToManyField(QuestionAuthor, verbose_name="Автор вопроса",
                                    related_name="question_authors")
    text = models.TextField("Текст вопроса")
    video_url = models.URLField("Ссылка на ютуб видео с вопросом")

    class Meta:
        verbose_name = "Вопрос"
        verbose_name_plural = "Вопросы"

    def __str__(self):
        return "Вопрос №" + str(self.id) + " Текст: " + str(self.text)


class Answer(models.Model):
    created_by = models.ForeignKey(User, verbose_name="Пользователь, который создал этот ответ",
                                   on_delete=models.SET_NULL, null=True)
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='answers')
    is_true = models.BooleanField("Ответ правильный/ошибочный", default=True)
    text = models.TextField("Текст ответа", default='')
    help_textV1 = models.TextField("Подсказка для упрощенного уровня", default='')
    help_textV2 = models.TextField("Подсказка для нормального уровня", default='')
    help_textV3 = models.TextField("Подсказка для усложненного уровня", default='')
    video_url = models.URLField("Ссылка на ютуб видео с ответом")
    check_queue = models.PositiveIntegerField("Очередь проверки, чем меньше - тем раньше вопрос будет проверен",
                                              default=0)
    HARD_LEVEL_OF_ANSWER = [
        ('EASY', 'Очевидный'),
        ('MEDIUM', 'Обычный'),
        ('HARD', 'Каверзный'),
    ]
    hard_level_of_answer = models.CharField(
        max_length=10, choices=HARD_LEVEL_OF_ANSWER, default='MEDIUM')

    class Meta:
        verbose_name = "Ответ"
        verbose_name_plural = "Ответы"

    def __str__(self):
        return "Ответ №" + str(self.id) + " Текст: " + str(self.textV1)
