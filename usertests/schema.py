import random

import graphene
from graphene_django import DjangoObjectType

from .models import *

from graphene_django.forms.mutation import DjangoModelFormMutation
from django import forms


class QuestionThemesNode(DjangoObjectType):
    class Meta:
        model = QuestionThemes


class QuestionAuthorNode(DjangoObjectType):
    class Meta:
        model = QuestionAuthor


class QuestionNode(DjangoObjectType):
    class Meta:
        model = Question


class AnswerNode(DjangoObjectType):
    class Meta:
        model = Answer


class UserTestQuery(graphene.ObjectType):
    """ Описываем запросы и возвращаемые типы данных """
    question_themes = graphene.List(QuestionThemesNode)
    question_author = graphene.List(QuestionAuthorNode)
    question_by_id = graphene.Field(QuestionNode, id=graphene.ID())
    answer = graphene.List(AnswerNode)

    def resolve_question_themes(self, info):
        try:
            print(info.context.user)
            print(info.context.user.user_access_level)
        except:
            pass
        return QuestionThemes.objects.all().order_by('-id')

    def resolve_question_author(self, info):
        try:
            print(info.context.user)
            print(info.context.user.user_access_level)
        except:
            pass
        return QuestionAuthor.objects.all().order_by('-id')

    def resolve_question_by_id(self, info, id):
        try:
            print(info.context.user)
            print(info.context.user.user_access_level)
        except:
            pass
        return Question.objects.get(pk=id)

    def resolve_answer(self, info):
        try:
            print(info.context.user)
            print(info.context.user.user_access_level)
        except:
            pass
        return Answer.objects.all()


# class UserTestMutation(graphene.ObjectType):
#     add_question_themes = graphene.Field(QuestionThemesNode,
#                                          name=graphene.String(required=True),
#                                          description=graphene.String())
#     add_question_author = graphene.Field(QuestionAuthorNode,
#                                          name=graphene.String(required=True))
#     add_question = graphene.Field(QuestionNode,
#                                   theme=graphene.String(),
#                                   author=graphene.String(),
#                                   text=graphene.String(),
#                                   video_url=graphene.String())
#
#
#     remove_question_themes = graphene.Field(graphene.Boolean, question_themes_id=graphene.ID())
#
#     def resolve_remove_question_themes(self, info, todo_id):
#         try:
#             QuestionThemes.objects.get(id=todo_id).delete()
#         except QuestionThemes.DoesNotExist:
#             return False
#         return True
#
class QuestionThemesFrom(forms.ModelForm):
    class Meta:
        model = QuestionThemes
        fields = '__all__'


class QuestionAuthorForm(forms.ModelForm):
    class Meta:
        model = QuestionAuthor
        fields = '__all__'


class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = '__all__'


class AnswerForm(forms.ModelForm):
    class Meta:
        model = Answer
        fields = '__all__'


class QuestionThemesMutation(DjangoModelFormMutation):
    question_themes = graphene.Field(QuestionThemesNode)

    class Meta:
        form_class = QuestionThemesFrom


class QuestionAuthorMutation(DjangoModelFormMutation):
    question_author = graphene.Field(QuestionAuthorNode)

    class Meta:
        form_class = QuestionAuthorForm


class QuestionMutation(DjangoModelFormMutation):
    question = graphene.Field(QuestionNode)

    class Meta:
        form_class = QuestionForm


class AnswerMutation(DjangoModelFormMutation):
    answer = graphene.Field(AnswerNode)

    class Meta:
        form_class = AnswerForm


class UserTestMutation(graphene.ObjectType):
    create_question_themes = QuestionThemesMutation.Field()
    update_question_themes = QuestionThemesMutation.Field()
    create_question_author = QuestionAuthorMutation.Field()
    update_question_author = QuestionAuthorMutation.Field()
    create_question = QuestionMutation.Field()
    update_question = QuestionMutation.Field()
    create_answer = AnswerMutation.Field()
    update_answer = AnswerMutation.Field()
