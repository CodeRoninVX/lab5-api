FROM python:3.11-slim
WORKDIR /app
COPY . .
RUN pip install -r requirements.txt
ENV MODE="comfort"
CMD ["python", "app.py"]