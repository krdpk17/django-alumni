FROM python:3
ENV PYTHONUNBUFFERED 1
WORKDIR /alumnisystem
ENV DJANGO_ALLOWED_HOSTS=localhost 127.0.0.1
COPY requirements.txt /alumnisystem/
RUN pip install -r requirements.txt
COPY ./alumnisystem/. /alumnisystem/
