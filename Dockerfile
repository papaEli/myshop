FROM python:3.12-slim
RUN groupadd -r groupdjango && useradd -r -g groupdjango userdj

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

RUN pip install --upgrade pip
WORKDIR /app/www/myshop
COPY requirements.txt .
RUN pip install -r requirements.txt

RUN pip install psycopg2-binary
COPY . .
USER userdj

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]