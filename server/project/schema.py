import strawberry
from strawberry_django.optimizer import DjangoOptimizerExtension


from apps.gridCRUD.graphql.schema import GridCRUDQuery


# 클래스 상속으로 각 장고 앱의 스키마 내용을 한 곳에 모음
# 클래스 상속; https://wikidocs.net/16073
@strawberry.type
class Query(GridCRUDQuery):  # class 자식클래스(부모클래스)
    """Query Root"""


schema = strawberry.Schema(
    query=Query,
    extensions=[
        DjangoOptimizerExtension,
    ],
)
