FROM python:3.10-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
CMD ["sh", "-c", "sleep 5 && alembic upgrade head && python app/main.py --host 0.0.0.0 --port 8000 --reload"]
