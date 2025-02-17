FROM python:3.12.8-slim

WORKDIR /app
COPY requirements.txt requirements.dev.txt /app/

RUN pip install --no-cache-dir -r requirements.txt -r requirements.dev.txt
COPY . /app/

EXPOSE 8000
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
