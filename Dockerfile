FROM python:3.10

WORKDIR /opt/app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY requirements.txt requirements.txt
COPY entrypoint.sh entrypoint.sh

RUN apt-get update && \
    apt-get install -y netcat-traditional

RUN  mkdir -p /var/www/static/ \
     && mkdir -p /var/www/media/ \
     && mkdir -p /opt/app/static/ \
     && mkdir -p /opt/app/media/ \
     && pip install --upgrade pip --no-cache-dir \
     && pip install -r requirements.txt --no-cache-dir

COPY . .

EXPOSE 8000
RUN chmod +x /opt/app/entrypoint.sh
ENTRYPOINT ["/opt/app/entrypoint.sh"]
