from flask import Flask, request, jsonify

app = Flask(__name__)

movies = {}  # Store movies in memory

@app.route('/movies', methods=['POST'])
def add_movie():
    movie = request.json
    movies[movie['id']] = movie
    return jsonify({"message": "Movie added successfully"}), 201

@app.route('/movies', methods=['GET'])
def get_movies():
    return jsonify(movies), 200

# @app.route('/movies', methods=['GET'])
# def get_movies():
#     return movies.to_json(orient='records'), 200

if __name__ == '__main__':
    app.run(port=5002)