# Dockerfile은 Docker 이미지가 빌드(build)될 때 거쳐야하는 단계를 정의하고 있는 텍스트 파일
# 추후 프로젝트에 반영 예정

# 기본 폼
FROM python:3
ENV PYTHONUNBUFFERED 1
WORKDIR /web
COPY . .
RUN pip install -r requirements.txt