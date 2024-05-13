# GraphQL 스키마 정의
# https://strawberry-graphql.github.io/strawberry-django/quick-start/#build-the-queries-and-schema
import strawberry
import strawberry_django

from server.apps.gridCRUD.graphql.types import DirectorType, FilmType


@strawberry.type
class GridCRUDQuery:  # 장고 앱 이름 + Query
    films: list[FilmType] = strawberry_django.field()
    directors: list[DirectorType] = strawberry_django.field()
