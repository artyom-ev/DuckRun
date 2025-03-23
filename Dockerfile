FROM python:3.9-slim

WORKDIR /app

COPY pyproject.toml uv.lock ./

RUN pip install --upgrade pip && \
    pip install uv && \
    uv sync

ENV PATH="/app/.venv/bin:$PATH"

COPY .env ./
COPY .streamlit ./
COPY app.py config.py menu.py ./
COPY assets ./assets
COPY pages ./pages

EXPOSE 8501

CMD ["sh", "-c", "streamlit run app.py --server.port=8501 --server.address=${SERVER_IP}"]