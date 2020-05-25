FROM python:3
ENV PYTHONUNBUFFERED 1
WORKDIR /alumnisystem
COPY requirements.txt /alumnisystem/
RUN pip install -r requirements.txt
COPY ./alumnisystem/. /alumnisystem/
