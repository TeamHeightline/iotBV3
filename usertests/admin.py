from django.contrib import admin
from django.contrib.auth.models import User
# Register your models here.
from .models import QuestionThemes, QuestionAuthor, Question, Answer


class MyModelAdmin(admin.ModelAdmin):
    # Делает так, чтобы staff-ы видели только свои вопросы и ответы, суперпользователь видит все ответы и вопросы
    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(created_by=request.user)

    # Делает так, чтобы в вопросах в поле автор можно было выбрать только своих авторов вопроса т.е. у человека
    # есть несколько авторов вопросов, он может приписать созданный вопрос только СВОИМ авторам
    def formfield_for_manytomany(self, db_field, request, **kwargs):
        if db_field.name == "author":
            user = User.objects.get(username=request.user)
            kwargs['queryset'] = QuestionAuthor.objects.filter(created_by=user)

        if db_field.name == "question":
            user = User.objects.get(username=request.user)
            kwargs['queryset'] = Question.objects.filter(created_by=user)

        return super(MyModelAdmin, self).formfield_for_manytomany(db_field, request, **kwargs)

    # Делает так, что в поле created_by можно выбрать только себя, и этот вариант стоит по дефолту
    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "created_by":
            kwargs["queryset"] = User.objects.filter(username=request.user)
            kwargs['initial'] = request.user
        return super().formfield_for_foreignkey(db_field, request, **kwargs)


# Регистрация моделей для того, чтобы их можно было смотреть в админ панели
admin.site.register(QuestionThemes, MyModelAdmin)

admin.site.register(QuestionAuthor, MyModelAdmin)

admin.site.register(Question, MyModelAdmin)

admin.site.register(Answer, MyModelAdmin)
