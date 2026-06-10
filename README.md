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