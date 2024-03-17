FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["gunicorn", "-b", "0.0.0.0:5002", "wsgi:app"]
# CMD ["gunicorn", "--timeout", "1000", "--workers=1", "-b", "0.0.0.0:5002", "--log-level", "debug", "manage", "wsgi:app"]