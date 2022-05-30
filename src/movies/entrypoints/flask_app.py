import sys
import db
from flask import Flask, request, jsonify
from adapters import models
from domain.commands import *
from domain.Invoker import *
from domain.model.Register import *
from domain.model.Login import *
from adapters import user_repository
import pandas as pd
from service.handlers import *

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
    first_genre = request.json["first genre"]
    second_genre = request.json["second genre"]        
    third_genre = request.json["third genre"]
    new_user = Invoker()
    register = Register()
    repo = user_repository.SqlAlchemyRepository(db.session)
    try:
        new_user.set_action(RegisterCommand(register, user_username, user_email, first_genre, second_genre, third_genre, repo))
        new_user.set_user()
    except(UsedUsername, UsedEmail, InvalidEmail) as e:
        return jsonify({"error" : str(e)}), 400
    return jsonify({"meesage" : "User registered!"}), 201
    
@app.route("/login", methods=["POST"])
def login_user():
    global preference_key
    user_username = request.json["username"]
    user_email = request.json["email"]
    registered_user = Invoker()
    login = Login()
    repo = user_repository.SqlAlchemyRepository(db.session)
    try:
        registered_user.set_action(LoginCommand(login, user_username, user_email, repo))
        registered_user.set_user()
    except(UserNotFound) as e:
        return jsonify({"error" : str(e)}), 400
    return jsonify({"message" : "Login succesful!"}), 200
    

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

