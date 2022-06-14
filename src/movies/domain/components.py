import pandas as pd
from .model.MoviesRatingFacade import *

class Component:
    def operation(self) -> pd.DataFrame:
        pass

class getMoviesByRecsComponent:
    def operation(self, preference_key : int, rating : str) -> pd.DataFrame:
        movies_result = pd.read_csv("movies/movie_results.csv")
        movies_based_on_pref_key = movies_result[movies_result['preference_key'] == preference_key]
        facade = Movies_Rating_Facade()
        movies_based_on_pref_key = facade.get_movies_based_on_rating(movies_based_on_pref_key,rating)
        movies_based_on_pref_key = movies_based_on_pref_key[["movie_title", "rating", "year"]]
        return movies_based_on_pref_key

class getMoviesByStarComponent:
    def operation(self, name : str, rating : str) -> pd.DataFrame:
        movies_result = pd.read_csv("movies/movie_results.csv")
        movies_based_on_star = movies_result[movies_result["star_cast"].str.contains(name)]
        facade = Movies_Rating_Facade()
        movies_based_on_star = facade.get_movies_based_on_rating(movies_based_on_star, rating)
        movies_based_on_star = movies_based_on_star[["movie_title", "rating", "year"]]
        return movies_based_on_star

class getMoviesByRating:
    def operation(self, low_rating : float, high_rating : float, rating : str) -> pd.DataFrame:
        movies_result = pd.read_csv("movies/movie_results.csv")
        movies_based_on_rating = movies_result[(movies_result["rating"] >= low_rating) & (movies_result["rating"] <= high_rating)]
        facade = Movies_Rating_Facade()
        movies_based_on_rating = facade.get_movies_based_on_rating(movies_based_on_rating, rating)
        movies_based_on_rating = movies_based_on_rating[["movie_title", "rating", "year"]]
        return movies_based_on_rating

class getMoviesByYear:
    def operation(self, year : int, rating: str) -> pd.DataFrame:
        movies_result = pd.read_csv("movie/movie_results.csv")
        movies_based_on_year = movies_result[movies_result["year"] == year]
        facade = Movies_Rating_Facade()
        movies_based_on_year = facade.get_movies_based_on_rating(movies_based_on_year, rating)
        movies_based_on_year = movies_based_on_year[["movie_title", "rating", "year"]]
        return movies_based_on_year