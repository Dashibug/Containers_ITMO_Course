FROM python:3.11-slim

RUN useradd -m appuser

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt


COPY app.py init_db.py ./

ENV APP_DATA_DIR=/data
VOLUME ["/data"]

USER appuser

EXPOSE 8000

CMD ["python", "app.py"]
