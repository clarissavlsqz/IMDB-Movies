from abc import ABC, abstractmethod
import pandas as pd
from .utils.FilterRating import *

# Open Close Principle - We can add other type of Movie Getters without modifying the existing ones
# Interface Segregation Principle - The types of Movie Getters fully depend on the abstract class Movies_Getter, meaning that is specific to its purpose

class Movies_Getter(ABC):
    @abstractmethod
    def get_movies():
        pass

class Movies_Recommendation(Movies_Getter):
    def get_movies(self, preference_key : int) -> pd.DataFrame:
        movies_result = pd.read_csv("movies/movie_results.csv")
        movies_based_on_pref_key = movies_result[movies_result['preference_key'] == preference_key]
        return movies_based_on_pref_key

class Movies_Cast(Movies_Getter):
    def get_movies(self, name : str) -> pd.DataFrame:
        movies_result = pd.read_csv("movies/movie_results.csv")
        movies_based_on_star = movies_result[movies_result["star_cast"].str.contains(name)]
        return movies_based_on_star

class Movies_Rating(Movies_Getter):
    def get_movies(self, low_rating : float, high_rating : float) -> pd.DataFrame:
        movies_result = pd.read_csv("movies/movie_results.csv")
        movies_based_on_rating = movies_result[(movies_result["rating"] >= low_rating) & (movies_result["rating"] <= high_rating)]
        return movies_based_on_rating

class Movies_Year(Movies_Getter):
    def get_movies(self, year : int) -> pd.DataFrame:
        movies_result = pd.read_csv("movies/movie_results.csv")
        movies_based_on_year = movies_result[movies_result["year"] == year]
        return movies_based_on_year