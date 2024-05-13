# GraphQL 타입 정의. Django 모델을 GraphQL 타입으로 변환. strawberry_django 라이브러리 사용(auto 데코레이터).
# 기본 https://strawberry-graphql.github.io/strawberry-django/quick-start/#define-types
# 상세 https://strawberry-graphql.github.io/strawberry-django/guide/fields/
from typing import List
import strawberry_django
from strawberry import auto

from apps.gridCRUD import models


# auto - (2)자동 적용
@strawberry_django.type(models.Film, fields="__all__")
class FilmType:
    pass


# # auto - (1)모든 필드 그대로 작성
# @strawberry_django.type(models.Film)  # models.Film 모델과 매핑
# class FilmType:
#     id: auto
#     title: auto
#     subtitle: auto
#     genre: auto
#     runningTime: auto
#     description: auto
#     posterImg: auto
#     release: auto
#     director_id: "Director"  # 아래 정의된 DirectorType 타입


@strawberry_django.type(models.Director)
class DirectorType:
    id: auto
    name: auto
    films: List[FilmType]  # 외래키 관련
