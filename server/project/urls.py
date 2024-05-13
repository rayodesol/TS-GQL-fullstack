# 앱이 아닌 프로젝트 성격의 URL 매핑만 추가되어야
from django.contrib import admin
from django.urls import include, path
from strawberry.django.views import AsyncGraphQLView

from .schema import schema

# Django의 URL 패턴 정의
urlpatterns = [
    path("admin/", admin.site.urls),
    # GraphQL 엔드포인트 설정; /graphql 엔드포인트에 대해 GraphQL 뷰를 정의하고, 해당 뷰에 schema.py에서 정의한 스키마를 연결
    path("graphql/", AsyncGraphQLView.as_view(schema=schema)),
    # grid_crud/로 시작하는 페이지 요청 시, apps/grid_crud/urls.py 파일의 매핑 정보를 읽어서 처리
    # path("grid_crud/", include("apps.gridCRUD.urls")),
]

"""
URL configuration for project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
