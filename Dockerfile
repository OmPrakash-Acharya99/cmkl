FROM python:3.11-slim

RUN useradd -r app  # Create a non-root user named "app"

WORKDIR /app

USER app  # Switch to the app user

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

EXPOSE 8000

CMD ["gunicorn", "--bind", "0.0.0.0:8000", "project.wsgi:application"]
