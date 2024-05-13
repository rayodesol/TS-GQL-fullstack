# 데이터베이스 모델 정의
# 필드 타입 https://docs.djangoproject.com/en/5.0/ref/models/fields/#model-field-types
# 필드 옵션 https://docs.djangoproject.com/en/5.0/topics/db/models/#field-options
from django.db import models


class Film(models.Model):
    # https://docs.djangoproject.com/en/5.0/topics/db/models/#automatic-primary-key-fields
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=300, help_text="영화 제목")
    subtitle = models.CharField(max_length=500, null=True, help_text="영화 부제목")
    genre = models.CharField(
        max_length=200, help_text="영화 장르"
    )  # -> TextChoicesField
    runningTime = models.IntegerField(help_text="영화 러닝 타임, minute")
    description = models.TextField(help_text="영화 줄거리 및 설명")
    # https://docs.djangoproject.com/en/5.0/ref/models/fields/#foreignkey   # ManyToManyField 관계로는?
    director = models.ForeignKey(
        "Director",
        on_delete=models.SET_NULL,
        null=True,
        related_name="films",  # 역참조
        help_text="제작자",
    )
    posterImg = models.URLField(
        max_length=700, help_text="포스터 이미지 URL"
    )  # -> ImageField
    release = models.DateField(help_text="개봉일")


class Director(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200, help_text="제작자 이름")
