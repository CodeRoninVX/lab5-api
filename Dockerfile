FROM python:3.11-slim
WORKDIR /app
COPY . .
RUN pip install -r requirements.txt
ENV MODE="comfort"
ENV AUTHOR="Akhмадзада Вахід"
ENV GROUP="АІ-232"
CMD ["python", "app.py"]