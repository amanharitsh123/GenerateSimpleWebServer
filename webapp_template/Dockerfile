FROM python:3.9-slim as base
FROM base as builder
WORKDIR /app
COPY . .
RUN pip install -r requirements.txt
ENTRYPOINT [ "python", "app.py" ]
EXPOSE 80