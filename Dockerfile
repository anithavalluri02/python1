
FROM python:3.11-slim

WORKDIR /app


COPY src/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt


COPY src/ .


EXPOSE 5000


CMD ["gunicorn", "--bind", "0.0.0.0:5000", "app.main:app"]
