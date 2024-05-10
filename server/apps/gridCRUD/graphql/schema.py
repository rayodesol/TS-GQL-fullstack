# GraphQL 스키마 정의
# https://strawberry-graphql.github.io/strawberry-django/quick-start/#build-the-queries-and-schema
import strawberry
import strawberry_django
from strawberry_django.optimizer import DjangoOptimizerExtension

from server.apps.gridCRUD.graphql.types import DirectorType, FilmType


@strawberry.type
class Query:
    films: list[FilmType] = strawberry_django.field()
    directors: list[DirectorType] = strawberry_django.field()


schema = strawberry.Schema(
    query=Query,
    extensions=[
        DjangoOptimizerExtension,
    ],
)
