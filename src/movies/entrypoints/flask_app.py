import sys
import db
from adapters.models import User
from flask import Flask, request, jsonify
from adapters import models
from movies import register_login
import domain.model.validate_email as validate_email
import pandas as pd

app = Flask(__name__)
models.start_mappers()

global preference_key 


@app.route("/hello", methods=["GET"])
def hello_world():
    return "Hello World!", 200

@app.route("/register_user", methods=["POST"])
def register_user():
    user_username = request.json["username"]
    user_email = request.json["email"]
    if validate_email.check(user_email):
        if register_login.username_exists_in_db(user_username):
           return jsonify({"error": "Username already exists"}), 400
        if register_login.email_exists_in_db(user_email):
            return jsonify({"error": "Email already used"}), 400
        register_login.getGenres()
        first_genre = request.json["first genre"]
        second_genre = request.json["second genre"]
        third_genre = request.json["third genre"]
        p_key = register_login.calculate_preference(first_genre, second_genre, third_genre)
        new_user = User(p_key, user_username, user_email)
        db.session.add(new_user)
        db.session.commit()

        return jsonify({"message": "User created"}), 201

    else:
        return jsonify({"error": "Email is not valid"}), 400

@app.route("/login", methods=["POST"])
def login_user():
    global preference_key
    user_username = request.json["username"]
    user_email = request.json["email"]
    if register_login.verify_user_is_registered(user_username, user_email):
        preference_key = register_login.getPreferenceKey(user_username, user_email)
        return jsonify({"message":"Login successful"})
    else:
        return jsonify({"error":"Invalid username or password"})

@app.route("/getMovieRecs/<int:preference_key>", methods=["GET"])
@app.route("/getMovieRecs/<int:preference_key>/<rating>", methods=["GET"])
def getMovieRecs(preference_key, rating = "True"):
    movies_result = pd.read_csv("movies/movie_results.csv")
    movies_based_on_pref_key = movies_result[movies_result['preference_key'] == preference_key]
    if rating == "False":
        movies_based_on_pref_key = movies_based_on_pref_key.sort_values(by=["rating"]).head(10)
    else:
       movies_based_on_pref_key = movies_based_on_pref_key.sort_values(by=["rating"], ascending=False).head(10)

    movies_based_on_pref_key = movies_based_on_pref_key[["movie_title", "rating", "year"]]
    
    return jsonify(movies_based_on_pref_key.to_dict(orient="records"))

@app.route("/getMoviesByStar/<name>", methods=["GET"])
@app.route("/getMoviesByStar/<name>/<rating>", methods=["GET"])
def getMoviesByStar(name, rating = "True"):
    movies_result = pd.read_csv("movies/movie_results.csv")
    movies_based_on_star = movies_result[movies_result["star_cast"].str.contains(name)]
    if movies_based_on_star.empty:
        return jsonify({"error" : "Movies not found with cast member"}), 404
    if rating == "False":
        movies_based_on_star = movies_based_on_star.sort_values(by=["rating"])
    else:
       movies_based_on_star = movies_based_on_star.sort_values(by=["rating"], ascending=False)

    movies_based_on_star = movies_based_on_star[["movie_title", "rating", "year"]]
    
    return jsonify(movies_based_on_star.to_dict(orient="records"))

@app.route("/getMoviesByRating/<float:low_rating>/<float:high_rating>", methods=["GET"])
@app.route("/getMoviesByRating/<float:low_rating>/<float:high_rating>/<rating>", methods=["GET"])
def getMoviesByRating(low_rating, high_rating, rating = "True"):
    movies_result = pd.read_csv("movies/movie_results.csv")
    movies_based_on_rating = movies_result[(movies_result["rating"] >= low_rating) & (movies_result["rating"] <= high_rating)]
    if movies_based_on_rating.empty:
        return jsonify({"error" : "Movies not found within range of rating"}), 404
    if rating == "False":
        movies_based_on_rating = movies_based_on_rating.sort_values(by=["rating"])
    else:
       movies_based_on_rating = movies_based_on_rating.sort_values(by=["rating"], ascending=False)

    movies_based_on_rating = movies_based_on_rating[["movie_title", "rating", "year"]]

    return jsonify(movies_based_on_rating.to_dict(orient="records"))

@app.route("/getMoviesByYear/<int:year>", methods=["GET"])
@app.route("/getMoviesByYear/<int:year>/<rating>", methods=["GET"])
def getMoviesByYear(year, rating = "True"):
    movies_result = pd.read_csv("movie/movie_results.csv")
    movies_based_on_year = movies_result[movies_result["year"] == year]
    if movies_based_on_year.empty:
        return jsonify({"error" : "Movies not found within the year"}), 404
    if rating == "False":
        movies_based_on_year = movies_based_on_year.sort_values(by=["rating"])
    else:
       movies_based_on_year = movies_based_on_year.sort_values(by=["rating"], ascending=False)

    movies_based_on_year = movies_based_on_year[["movie_title", "rating", "year"]]

    return jsonify(movies_based_on_year.to_dict(orient="records"))

