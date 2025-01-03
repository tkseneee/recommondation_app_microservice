# from flask import Flask, jsonify
# import pandas as pd
# import requests
# from sklearn.metrics.pairwise import cosine_similarity

# app = Flask(__name__)

# @app.route('/recommend/<int:user_id>', methods=['GET'])
# def recommend(user_id):
#     response = requests.get('http://localhost:5003/ratings')
#     ratings = pd.DataFrame(response.json())
#     if ratings.empty:
#         return jsonify({"message": "No ratings available"}), 404

#     user_movie_matrix = ratings.pivot_table(index='user_id', columns='movie_id', values='rating').fillna(0)
#     if user_id not in user_movie_matrix.index:
#         return jsonify({"message": "User not found"}), 404

#     similarity = cosine_similarity(user_movie_matrix)
#     user_similarities = similarity[user_id - 1]
#     similar_users = sorted(enumerate(user_similarities), key=lambda x: x[1], reverse=True)[1:4]

#     recommendations = []
#     for similar_user in similar_users:
#         similar_user_id = similar_user[0] + 1
#         similar_user_movies = ratings[ratings['user_id'] == similar_user_id]['movie_id'].tolist()
#         recommendations.extend(similar_user_movies)

#     return jsonify({"recommendations": list(set(recommendations))}), 200


# if __name__ == '__main__':
#     app.run(port=5005)

from flask import Flask, jsonify
import pandas as pd
import requests
from sklearn.metrics.pairwise import cosine_similarity

app = Flask(__name__)

@app.route('/recommend/<int:user_id>', methods=['GET'])
def recommend(user_id):
    # Fetch ratings from the Rating Service
    response = requests.get('http://localhost:5003/ratings')
    
    ratings = pd.DataFrame(response.json())

    # Create user-item matrix
    user_movie_matrix = ratings.pivot_table(index='user_id', columns='movie_id', values='rating').fillna(0)


    # Calculate cosine similarity between users
    similarity = cosine_similarity(user_movie_matrix)
    
    # Get the similarities for the specified user
    user_similarities = similarity[user_id - 1]
    
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


