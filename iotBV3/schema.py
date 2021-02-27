import graphene

from usertests.schema import Query, Mutation

schema = graphene.Schema(query=Query, mutation=Mutation)