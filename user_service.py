from flask import Flask, request, jsonify

app = Flask(__name__)

users = {}  # Store users in memory

@app.route('/users', methods=['POST'])
def add_user():
    user = request.json
    users[user['id']] = user
    return jsonify({"message": "User added successfully"}), 201

if __name__ == '__main__':
    app.run(port=5001)
    