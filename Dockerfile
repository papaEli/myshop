# Используем официальный образ Python
FROM python:3.10

# Рабочая директория
WORKDIR /opt/app

# Отключаем запись .pyc файлов и буферизацию вывода
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Копируем зависимости и скрипты
COPY requirements.txt .
COPY entrypoint.sh .

# Устанавливаем системные зависимости и Python-пакеты
RUN apt-get update && \
    apt-get install -y netcat-traditional && \
    mkdir -p /var/www/static/ /var/www/media/ /opt/app/static/ /opt/app/media/ && \
    pip install --upgrade pip && \
    pip install -r requirements.txt

# Копируем весь проект
COPY . .

# Исправляем перевод строк и права для entrypoint.sh
RUN sed -i 's/\r$//' /opt/app/entrypoint.sh && \
    chmod +x /opt/app/entrypoint.sh

# Открываем порт
EXPOSE 8000

# Запускаем entrypoint.sh через shell (для Windows-совместимости)
ENTRYPOINT ["/bin/sh", "/opt/app/entrypoint.sh"]