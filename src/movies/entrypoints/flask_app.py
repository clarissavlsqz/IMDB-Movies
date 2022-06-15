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
from domain.model.Movies_Getter_Facade import *

app = Flask(__name__)
models.start_mappers()

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
    facade = Movies_Getter_Facade()
    movies_result = facade.get_movies("recommendation", rating, preference_key)
    return jsonify(movies_result)

@app.route("/getMoviesByStar/<name>", methods=["GET"])
@app.route("/getMoviesByStar/<name>/<rating>", methods=["GET"])
def getMoviesByStar(name, rating = "True"):
    facade = Movies_Getter_Facade()
    movies_result = facade.get_movies("star cast", rating, None, name)
    if len(movies_result) == 0:
        return jsonify({"error" : "Movies not found with cast member"}), 404
    return jsonify(movies_result)

@app.route("/getMoviesByRating/<float:low_rating>/<float:high_rating>", methods=["GET"])
@app.route("/getMoviesByRating/<float:low_rating>/<float:high_rating>/<rating>", methods=["GET"])
def getMoviesByRating(low_rating, high_rating, rating = "True"):
    facade = Movies_Getter_Facade()
    movies_result = facade.get_movies("rating", rating, None, None, low_rating, high_rating)
    if len(movies_result) == 0:
        return jsonify({"error" : "Movies not found within range of rating"}), 404
    return jsonify(movies_result)

@app.route("/getMoviesByYear/<int:year>", methods=["GET"])
@app.route("/getMoviesByYear/<int:year>/<rating>", methods=["GET"])
def getMoviesByYear(year, rating = "True"):
    facade = Movies_Getter_Facade()
    movies_result = facade.get_movies("year", rating, None, None, None, None, year)
    if len(movies_result) == 0:
        return jsonify({"error" : "Movies not found within the year"}), 404
    return jsonify(movies_result)

