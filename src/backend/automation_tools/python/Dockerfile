FROM python:3.11-slim

WORKDIR /app

COPY pyproject.toml poetry.lock ./
RUN pip install poetry && poetry install

COPY . src/

CMD ["poetry", "run", "python", "src/app.py"]