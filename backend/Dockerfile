FROM python:3.12-slim

WORKDIR /movie_recommender

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY app/ /movie_recommender/app

WORKDIR /movie_recommender/app

# The user will need to set the GOOGLE_API_KEY environment variable when running the container
ENV GOOGLE_API_KEY=""

EXPOSE 8501:8501

CMD ["streamlit", "run", "ui.py"]

