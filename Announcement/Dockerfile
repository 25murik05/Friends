FROM python:3.10

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1


WORKDIR /app

COPY . .

RUN pip install -r requirements.txt

RUN python manage.py migrate

RUN python manage.py makemigrations

#EXPOSE 8000
#
#CMD ["python", "manage.py", "runserver"]