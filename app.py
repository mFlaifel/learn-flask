from flask import Flask, request, jsonify
import uuid

app = Flask(__name__)

todo_items = {}


@app.route('/')
def welcome():
    return 'Todo app API'

@app.route('/items', methods=['GET'])
def get_items():
    return jsonify(list(todo_items.values()))


@app.route('/items/<item_id>', methods=['GET'])
def get_item(item_id):
    item = todo_items.get(item_id)
    if not item:
        return jsonify({'error': 'Item not found'}), 404
    return jsonify(item)

@app.route('/items', methods=['POST'])
def add_item():
    data = request.get_json()
    if not data or 'task' not in data:
        return jsonify({'error': 'Task is required'}), 400

    item_id= str(uuid.uuid4())
    new_item={
        'id':item_id,
        'task':data['task'],
        'completed':False
    }
    todo_items[item_id]=new_item
    return jsonify(new_item),201


@app.route('/items/<item_id>', methods=['PUT'])
def update_item(item_id):
    item = todo_items.get(item_id)
    if not item:
        return jsonify({'error': 'Item not found'}), 404

    data = request.get_json()
    if not data or 'task' not in data:
        return jsonify({'error': 'Task is required'}), 400

    item['task'] = data['task']
    item['completed'] = data.get('completed', item['completed'])
    todo_items[item_id] = item
    return jsonify(item)


@app.route('/items/<item_id>', methods=['DELETE'])
def delete_item(item_id):
    item = todo_items.pop(item_id, None)
    if not item:
        return jsonify({'error': 'Item not found'}), 404
    del todo_items[item_id]
    return jsonify({'message': 'Item deleted successfully'}), 200

if __name__ == '__main__':
    app.run(host='127.0.0.5', port=5005, debug=True)
