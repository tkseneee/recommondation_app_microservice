from flask import Flask, request, jsonify
import pandas as pd

app = Flask(__name__)

ratings = pd.DataFrame(columns=['user_id', 'movie_id', 'rating'])

@app.route('/ratings', methods=['POST'])
def add_rating():
    global ratings
    data = request.json
    new_rating = pd.DataFrame([data])
    ratings = pd.concat([ratings, new_rating], ignore_index=True)
    return jsonify({"message": "Rating added successfully"}), 201

@app.route('/ratings', methods=['GET'])
def get_ratings():
    return ratings.to_json(orient='records'), 200

# @app.route('/ratings', methods=['GET'])
# def get_ratings():
#     return jsonify(ratings), 200

if __name__ == '__main__':
    app.run(port=5003)
