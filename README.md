# Recommendation App Microservice

This project is a **movie recommendation system** implemented using **Flask** microservices. It consists of multiple services that handle user data, movie data, ratings, and recommendation logic.

## Table of Contents

- [Project Overview](#project-overview)
- [Architecture](#architecture)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Running the Microservices](#running-the-microservices)
- [API Endpoints](#api-endpoints)
- [Testing the Microservices](#testing-the-microservices)
- [Contributing](#contributing)
- [License](#license)

---

## Project Overview

This microservices-based recommendation system enables:
- **User Management**: Adding and retrieving users.
- **Movie Management**: Adding and retrieving movies.
- **Ratings**: Users can rate movies.
- **Recommendation Engine**: Uses **collaborative filtering** with **cosine similarity** to recommend movies to users.

---

## Architecture

The project consists of **five microservices**:
1. **User Service (Port: 5001)** - Manages users.
2. **Item (Movie) Service (Port: 5002)** - Stores movie details.
3. **Rating Service (Port: 5003)** - Handles user ratings for movies.
4. **Recommendation Model Service (Port: 5004)** - Generates the **user similarity matrix**.
5. **Recommendation to User Service (Port: 5005)** - Uses the similarity matrix to suggest movies.

The **main script (`main.py`)** starts all these services.

---

## Prerequisites

Ensure you have the following installed:
- **Python 3.x**
- **Flask**
- **pandas**
- **requests**
- **scikit-learn**
- **Git (for version control)**

---

## Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/tkseneee/recommondation_app_microservice.git
   cd recommondation_app_microservice

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt

---

## Running the Microservices

**To start all services at once, run:**
   ```bash
   python main.py

This will launch all microservices in separate subprocesses.

**Alternatively, you can start each service manually:**

   ```bash
   python user_service.py
   python item_service.py
   python rating_service.py
   python recommondation_model_service.py
   python recommend_to_user_service.py

---

## API Endpoints

1. **User Service (Port: 5001)**
   ```bash
   curl -X POST http://localhost:5001/users -H "Content-Type: application/json" -d "{\"id\": 1, \"name\": \"Senthil\"}"
   curl -X POST http://localhost:5001/users -H "Content-Type: application/json" -d "{\"id\": 2, \"name\": \"Kumar\"}"
   curl -X POST http://localhost:5001/users -H "Content-Type: application/json" -d "{\"id\": 3, \"name\": \"Raju\"}"
   curl -X POST http://localhost:5001/users -H "Content-Type: application/json" -d "{\"id\": 4, \"name\": \"Ramya\"}"

2. **Item Service (Port: 5002)**
   ```bash
   curl -X POST http://localhost:5002/movies -H "Content-Type: application/json" -d "{\"id\": 103, \"title\": \"Avenger\"}"
   curl -X POST http://localhost:5002/movies -H "Content-Type: application/json" -d "{\"id\": 104, \"title\": \"Spyderman\"}"
   curl -X POST http://localhost:5002/movies -H "Content-Type: application/json" -d "{\"id\": 105, \"title\": \"Polar Express\"}"
   curl -X POST http://localhost:5002/movies -H "Content-Type: application/json" -d "{\"id\": 106, \"title\": \"Lion King\"}"
   curl -X POST http://localhost:5002/movies -H "Content-Type: application/json" -d "{\"id\": 101, \"title\": \"Inception\"}"
   curl -X POST http://localhost:5002/movies -H "Content-Type: application/json" -d "{\"id\": 102, \"title\": \"Davincicode\"}"

3. **Rating Service (Port: 5003)**
   ```bash
   curl -X POST http://localhost:5003/ratings -H "Content-Type: application/json" -d "{\"user_id\": 1, \"movie_id\": 105, \"rating\": 5}"
   curl -X POST http://localhost:5003/ratings -H "Content-Type: application/json" -d "{\"user_id\": 1, \"movie_id\": 103, \"rating\": 2}"
   curl -X POST http://localhost:5003/ratings -H "Content-Type: application/json" -d "{\"user_id\": 2, \"movie_id\": 103, \"rating\": 4}"
   curl -X POST http://localhost:5003/ratings -H "Content-Type: application/json" -d "{\"user_id\": 2, \"movie_id\": 105, \"rating\": 1}"
   curl -X POST http://localhost:5003/ratings -H "Content-Type: application/json" -d "{\"user_id\": 3, \"movie_id\": 103, \"rating\": 1}"

4. **Recommendation Model Service (Port: 5004)**
   To generate user-item simmilarity matrix
   ```bash
   curl -X GET http://localhost:5004/generate_similarity

   To view the simmilarity matrix
   ```bash
   curl -X GET http://localhost:5004/view_similarity

5. **Recommendation to User Service (Port: 5005)**
   Get movie recommendations for a user
   ```bash
   curl -X GET http://localhost:5005/recommend/1

---

## Notes

**The services communicate via HTTP requests, so ensure that all services are running before making requests.**
**You can modify the similarity calculation in recommondation_model_service.py if needed. Even can use any other recommendation model there**

---

## Author
**Created by Dr T.K.Senthil Kumar**
**GitHub: tkseneee**

---
