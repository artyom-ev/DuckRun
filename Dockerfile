# Используем официальный образ Python
FROM python:3.9-slim

# Устанавливаем рабочую директорию в контейнере
WORKDIR /app

# Копируем только необходимые файлы для установки зависимостей
COPY pyproject.toml uv.lock ./

# Устанавливаем uv и синхронизируем зависимости
RUN pip install --upgrade pip && \
    pip install uv && \
    uv sync

ENV PATH="/app/.venv/bin:$PATH"

# Копируем только нужные файлы и папки
COPY .env ./
COPY .streamlit ./
COPY app.py config.py menu.py ./
COPY assets ./assets
COPY pages ./pages

# Открываем порт, на котором работает Streamlit
EXPOSE 8501

# Команда для запуска Streamlit
CMD ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]