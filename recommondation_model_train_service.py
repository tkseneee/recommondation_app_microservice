from flask import Flask, jsonify
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity

app = Flask(__name__)

user_movie_matrix = None
similarity_matrix = None

@app.route('/train', methods=['POST'])
def train_model():
    global user_movie_matrix, similarity_matrix
    # Mock rating data fetch
    ratings = pd.read_json('http://localhost:5003/ratings')
    user_movie_matrix = ratings.pivot_table(index='user_id', columns='movie_id', values='rating').fillna(0)
    similarity_matrix = cosine_similarity(user_movie_matrix)
    return jsonify({"message": "Model trained successfully"}), 200

if __name__ == '__main__':
    app.run(port=5004)
