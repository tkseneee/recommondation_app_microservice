from flask import Flask, jsonify
import pandas as pd
import requests
from sklearn.metrics.pairwise import cosine_similarity

app = Flask(__name__)
similarity_matrix = []

@app.route('/generate_similarity', methods=['GET'])
def generate_similarity():
    # Fetch ratings from the Rating Service (5003)
    response = requests.get('http://localhost:5003/ratings')
    ratings = pd.DataFrame(response.json())

    # Create user-item matrix
    user_movie_matrix = ratings.pivot_table(index='user_id', columns='movie_id', values='rating').fillna(0)

    # Calculate cosine similarity between users
    global similarity_matrix
    similarity_matrix = cosine_similarity(user_movie_matrix).tolist()

    return jsonify({"message": "Similarity matrix generated"}), 200

@app.route('/view_similarity', methods=['GET'])
def view_similarity():
    return jsonify(similarity_matrix), 200

if __name__ == '__main__':
    app.run(port=5004)