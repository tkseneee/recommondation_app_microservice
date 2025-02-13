from flask import Flask, jsonify, request
import pandas as pd
import requests

app = Flask(__name__)
similarity_matrix = []

@app.route('/receive_similarity', methods=['POST'])
def receive_similarity():
    global similarity_matrix
    similarity_matrix = request.json
    return jsonify({"message": "Similarity matrix received successfully"}), 200

@app.route('/recommend/<int:user_id>', methods=['GET'])
def recommend(user_id):
    # Fetch ratings from the Rating Service (5003)
    response = requests.get('http://localhost:5003/ratings')
    ratings = pd.DataFrame(response.json())

    # Generate similarity matrix if not available
    if not similarity_matrix:
        similarity_response = requests.get('http://localhost:5004/generate_similarity')
        if similarity_response.status_code != 200:
            return jsonify({"error": "Failed to generate similarity matrix"}), 500

        # Fetch the generated similarity matrix
        similarity_view_response = requests.get('http://localhost:5004/view_similarity')
        similarity_matrix.clear()
        similarity_matrix.extend(similarity_view_response.json())

    # Get the similarities for the specified user
    user_similarities = similarity_matrix[user_id - 1]

    # Get similar users
    similar_users = sorted(enumerate(user_similarities), key=lambda x: x[1], reverse=True)[1:4]

    # Get all movies watched by the user
    user_watched_movies = ratings[ratings['user_id'] == user_id]['movie_id'].tolist()

    recommendations = []
    for similar_user in similar_users:
        similar_user_id = similar_user[0] + 1  # Index + 1 for user_id
        # Get movies watched by the similar user
        similar_user_movies = ratings[ratings['user_id'] == similar_user_id]['movie_id'].tolist()

        # Filter out movies that the user has already watched
        filtered_movies = [movie for movie in similar_user_movies if movie not in user_watched_movies]

        recommendations.extend(filtered_movies)

    # Remove duplicate movie recommendations
    recommendations = list(set(recommendations))

    return jsonify({"recommendations": recommendations}), 200

if __name__ == '__main__':
    app.run(port=5005)