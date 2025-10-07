FROM python:3.14-rc-slim-bookworm

ENV PYTONONDONTWRITEBYTECODE=1 \
PYTONUNBUFFERED=1

WORKDIR /app

RUN apt-get update && apt-get install -y docker.io curl

COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

COPY src/requirements.txt .
RUN uv pip install -r requirements.txt --system

COPY src/ .

EXPOSE 8000

CMD [ "python", "manage.py", "runserver", "0.0.0.0:8000" ]

