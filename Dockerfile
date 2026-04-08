FROM python:3.12-slim

WORKDIR /movie_recommender

COPY pyproject.toml uv.lock ./

RUN pip install --no-cache-dir uv

RUN uv sync --frozen

COPY app/ /movie_recommender/app

WORKDIR /movie_recommender/app

# The user will need to set the GOOGLE_API_KEY environment variable when running the container
ENV GOOGLE_API_KEY=""

EXPOSE 8501


