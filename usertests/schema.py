import random

import graphene
from graphene_django import DjangoObjectType

from .models import *


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


class UserTestMutation(graphene.ObjectType):
    add_question_themes = graphene.Field(QuestionThemesNode,
                                         name=graphene.String(required=True),
                                         description=graphene.String())
    remove_question_themes = graphene.Field(graphene.Boolean, question_themes_id=graphene.ID())

    def resolve_remove_question_themes(self, info, todo_id):
        try:
            QuestionThemes.objects.get(id=todo_id).delete()
        except QuestionThemes.DoesNotExist:
            return False
        return True
