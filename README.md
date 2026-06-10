# Лабораторна робота №5-6
# Модель: Метод Гауса (5 семестр)
# Автор: Ахмадзада Вахід, група АІ-232

## Тема
CI/CD Pipeline + Flask API

## Модель
Метод Гауса (5 семестр)

## Автор
Ахмадзада Вахід, група АІ-232

## Варіант
Непарний → додатковий етап тестування (pytest)

## Як запустити локально
pip install -r requirements.txt
python app.py

## Як запустити тести
pytest test_app.py -v

## CI/CD
Pipeline автоматично запускається при push у гілку main.
Етапи: install → syntax check → pytest → docker build

## Cloud Deployment

Платформа: Render (free tier)
Публічний URL: https://devops-232-akhmadzada.onrender.com
Endpoint: POST https://devops-232-akhmadzada.onrender.com/calculate
Тип deployment: Manual Docker deployment

## Тестовий запит
curl -X POST https://devops-232-akhmadzada.onrender.com/calculate \
  -H "Content-Type: application/json" \
  -d '{"matrix":[[2,1,-1],[-3,-1,2],[-2,1,2]],"vector":[8,-11,-3]}'