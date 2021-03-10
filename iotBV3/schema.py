import graphene

from usertests.schema import  UserTestMutation, UserTestQuery
from users.schema import AuthMutation, AuthQuery


class Mutation(AuthMutation, UserTestMutation, graphene.ObjectType):
    pass


class Query(UserTestQuery, AuthQuery, graphene.ObjectType):
    pass


schema = graphene.Schema(query=Query, mutation=Mutation)
