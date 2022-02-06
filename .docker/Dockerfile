FROM python:3.10

ENV APP_HOME /app
WORKDIR $APP_HOME

ENV PYTHONUNBUFFERED 1

RUN apt-get update -y && apt-get install -y -- \
    gettext \
    git \
    build-essential \
    default-libmysqlclient-dev \
    python3-psycopg2 \
    libpq-dev \

COPY ../requirements requirements
COPY ../requirements.txt .
RUN pip3 install --upgrade pip && \
    pip3 install --no-cache-dir -r requirements.txt

COPY ../ .

ENV PORT=8000
EXPOSE 8000

CMD exec gunicorn --bind 0.0.0.0:$PORT --workers 1 --threads 8 --timeout 0 setup.wsgi:application