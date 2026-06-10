# Модель: Метод Гауса (5 семестр)
# Автор: Ахмадзада Вахід, група АІ-232
# Варіант: JSON POST-запит (непарний номер у списку)

from flask import Flask, request, jsonify

app = Flask(__name__)
app.json.ensure_ascii = False


def gauss_elimination(matrix, vector):
    """Метод Гауса для розв'язання системи лінійних рівнянь Ax = b"""
    n = len(vector)
    aug = [matrix[i][:] + [vector[i]] for i in range(n)]

    # Прямий хід
    for col in range(n):
        max_row = max(range(col, n), key=lambda r: abs(aug[r][col]))
        aug[col], aug[max_row] = aug[max_row], aug[col]

        for row in range(col + 1, n):
            if abs(aug[col][col]) < 1e-12:
                continue

            factor = aug[row][col] / aug[col][col]

            for j in range(col, n + 1):
                aug[row][j] -= factor * aug[col][j]

    # Зворотний хід
    x = [0.0] * n

    for i in range(n - 1, -1, -1):
        x[i] = aug[i][n]

        for j in range(i + 1, n):
            x[i] -= aug[i][j] * x[j]

        x[i] /= aug[i][i]

    return x


@app.route('/', methods=['GET'])
def index():
    return jsonify({
        "service": "Метод Гауса API",
        "author": "Ахмадзада Вахід, група АІ-232",
        "endpoint": "POST /calculate",
        "example": {
            "matrix": [[2, 1, -1], [-3, -1, 2], [-2, 1, 2]],
            "vector": [8, -11, -3]
        }
    })


@app.route('/calculate', methods=['POST'])
def calculate():
    data = request.get_json()

    if not data:
        return jsonify({
            "error": "Потрібно надіслати JSON"
        }), 400

    matrix = data.get('matrix')
    vector = data.get('vector')

    if matrix is None or vector is None:
        return jsonify({
            "error": "Потрібні поля: matrix та vector"
        }), 400

    if len(matrix) != len(vector):
        return jsonify({
            "error": "Розміри matrix і vector не співпадають"
        }), 400

    try:
        solution = [round(x, 1) for x in gauss_elimination(matrix, vector)]

        return jsonify({
            "author": "Ахмадзада Вахід, група АІ-232",
            "input": {
                "matrix": matrix,
                "vector": vector
            },
            "model": "Метод Гауса",
            "variant": "POST JSON (непарний)",
            "solution": solution
        })

    except Exception as e:
        return jsonify({
            "error": str(e)
        }), 500


if __name__ == '__main__':
    print("Сервер запущено: http://127.0.0.1:5000")
    print("Endpoint: POST http://127.0.0.1:5000/calculate")

    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port, debug=False)
