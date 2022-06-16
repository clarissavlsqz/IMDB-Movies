import sys
import db
from domain.model.GetPKeyFacade import *
from domain.model.LoginFacade import *
from domain.model.RegisterFacade import *
from domain.model.VerifyUser import *
from flask import Flask, request, jsonify
from adapters import models
from service.handlers import *
from domain.model.Movies_Getter_Facade import *

app = Flask(__name__)
models.start_mappers()

@app.route("/hello", methods=["GET"])
def hello_world():
    return "Hello World!", 200

@app.route("/register_user", methods=["POST"])
def register_user():
    print("1.- Comedy\n2.- Drama\n3.- Sci-Fi\n4.- Romance\n5.- Drama")
    user_username = request.json["username"]
    user_email = request.json["email"]
    first_genre = request.json["first genre"]
    second_genre = request.json["second genre"]        
    third_genre = request.json["third genre"]
    register_facade = Register_Facade()
    try:
        register_facade.register_user(user_username, user_email, first_genre, second_genre, third_genre)
    except(UsedUsername, UsedEmail, InvalidEmail) as e:
        return jsonify({"error" : str(e)}), 400
    return jsonify({"meesage" : "User registered!"}), 201
    
@app.route("/login", methods=["POST"])
def login_user():
    global preference_key
    user_username = request.json["username"]
    user_email = request.json["email"]
    login_facade = Login_Facade()
    try:
       login_facade.login_user(user_username, user_email)
    except(UserNotFound) as e:
        return jsonify({"error" : str(e)}), 400
    return jsonify({"message" : "Login succesful!"}), 200
    

@app.route("/getMovieRecs", methods=["GET"])
@app.route("/getMovieRecs/<rating>", methods=["GET"])
def getMovieRecs(rating = "True"):
    # We ask for email as a way to make user the endpoint is used by a user
    user_email = request.json["email"]
    repo = user_repository.SqlAlchemyRepository(db.session)
    facade = Get_PKey_Facade()
    try:
        preference_key = facade.get_preference_key(user_email, repo)
    except(UserNotFound) as e:
        return jsonify({"error" : str(e)}), 400
    facade = Movies_Getter_Facade()
    movies_result = facade.get_movies("recommendation", rating, preference_key)
    return jsonify(movies_result[:10])
   

@app.route("/getMoviesByStar/<name>", methods=["GET"])
@app.route("/getMoviesByStar/<name>/<rating>", methods=["GET"])
def getMoviesByStar(name, rating = "True"):
    # We ask for email as a way to make user the endpoint is used by a user
    user_email = request.json["email"]
    repo = user_repository.SqlAlchemyRepository(db.session)
    facade = Verify_User_Facade()
    try:
        facade.verify_user(user_email, repo)
    except(UserNotFound) as e:
        return jsonify({"error" : str(e)}), 400
    facade = Movies_Getter_Facade()
    movies_result = facade.get_movies("star cast", rating, None, name)
    if len(movies_result) == 0:
        return jsonify({"error" : "Movies not found with cast member"}), 404
    return jsonify(movies_result)

@app.route("/getMoviesByRating/<float:low_rating>/<float:high_rating>", methods=["GET"])
@app.route("/getMoviesByRating/<float:low_rating>/<float:high_rating>/<rating>", methods=["GET"])
def getMoviesByRating(low_rating, high_rating, rating = "True"):
    # We ask for email as a way to make user the endpoint is used by a user
    user_email = request.json["email"]
    repo = user_repository.SqlAlchemyRepository(db.session)
    facade = Verify_User_Facade()
    try:
        facade.verify_user(user_email, repo)
    except(UserNotFound) as e:
        return jsonify({"error" : str(e)}), 400
    facade = Movies_Getter_Facade()
    movies_result = facade.get_movies("rating", rating, None, None, low_rating, high_rating)
    if len(movies_result) == 0:
        return jsonify({"error" : "Movies not found within range of rating"}), 404
    return jsonify(movies_result)

@app.route("/getMoviesByYear/<int:year>", methods=["GET"])
@app.route("/getMoviesByYear/<int:year>/<rating>", methods=["GET"])
def getMoviesByYear(year, rating = "True"):
    # We ask for email as a way to make user the endpoint is used by a user
    user_email = request.json["email"]
    repo = user_repository.SqlAlchemyRepository(db.session)
    facade = Verify_User_Facade()
    try:
        facade.verify_user(user_email, repo)
    except(UserNotFound) as e:
        return jsonify({"error" : str(e)}), 400
    facade = Movies_Getter_Facade()
    movies_result = facade.get_movies("year", rating, None, None, None, None, year)
    if len(movies_result) == 0:
        return jsonify({"error" : "Movies not found within the year"}), 404
    return jsonify(movies_result)

