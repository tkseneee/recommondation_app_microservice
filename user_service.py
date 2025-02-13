from flask import Flask, request, jsonify

app = Flask(__name__)

users = {}  # Store users in memory

@app.route('/users', methods=['POST'])
def add_user():
    user = request.json
    users[user['id']] = user
    return jsonify({"message": "User added successfully"}), 201

@app.route('/users', methods=['GET'])
def get_users():
    return jsonify(users), 200

if __name__ == '__main__':
    app.run(port=5001)

#curl -X POST http://localhost:5001/users -H "Content-Type: application/json" -d "{\"id\": 1, \"name\": \"Senthil\"}"