# Тести для Методу Гауса
# Автор: Ахмадзада Вахід, група АІ-232

import sys
import os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from app import app, gauss_elimination
import json

def test_gauss_basic():
    """Перевіряємо що метод Гауса правильно розв'язує систему"""
    A = [[2, 1, -1], [-3, -1, 2], [-2, 1, 2]]
    b = [8, -11, -3]
    result = gauss_elimination(A, b)
    assert abs(result[0] - 2.0) < 1e-6
    assert abs(result[1] - 3.0) < 1e-6
    assert abs(result[2] - (-1.0)) < 1e-6

def test_api_calculate():
    """Перевіряємо що API endpoint /calculate працює"""
    client = app.test_client()
    payload = {
        "matrix": [[2, 1, -1], [-3, -1, 2], [-2, 1, 2]],
        "vector": [8, -11, -3]
    }
    response = client.post(
        '/calculate',
        data=json.dumps(payload),
        content_type='application/json'
    )
    assert response.status_code == 200
    data = json.loads(response.data)
    assert "solution" in data
    assert abs(data["solution"][0] - 2.0) < 1e-6

def test_api_missing_fields():
    """Перевіряємо що API повертає помилку якщо дані неповні"""
    client = app.test_client()
    response = client.post(
        '/calculate',
        data=json.dumps({"matrix": [[1, 2], [3, 4]]}),
        content_type='application/json'
    )
    assert response.status_code == 400