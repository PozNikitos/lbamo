from flask import Flask, jsonify, request

app = Flask(__name__)

# Пример данных
items = [
    {"id": 1, "name": "Item 1", "description": "Description for item 1"},
    {"id": 2, "name": "Item 2", "description": "Description for item 2"}
]

# Получить все элементы
@app.route('/items', methods=['GET'])
def get_items():
    return jsonify(items), 200

# Получить элемент по ID
@app.route('/items/<int:item_id>', methods=['GET'])
def get_item(item_id):
    item = next((item for item in items if item["id"] == item_id), None)
    if item:
        return jsonify(item), 200
    else:
        return jsonify({"message": "Item not found"}), 404

# Добавить новый элемент
@app.route('/items', methods=['POST'])
def add_item():
    new_item = request.json
    new_item['id'] = len(items) + 1
    items.append(new_item)
    return jsonify(new_item), 201

# Обновить элемент по ID
@app.route('/items/<int:item_id>', methods=['PUT'])
def update_item(item_id):
    item = next((item for item in items if item["id"] == item_id), None)
    if item:
        updated_data = request.json
        item.update(updated_data)
        return jsonify(item), 200
    else:
        return jsonify({"message": "Item not found"}), 404

# Удалить элемент по ID
@app.route('/items/<int:item_id>', methods=['DELETE'])
def delete_item(item_id):
    global items
    items = [item for item in items if item["id"] != item_id]
    return jsonify({"message": "Item deleted"}), 200

# Запуск сервера
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
