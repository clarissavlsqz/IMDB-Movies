import pandas as pd
from domain.model.Simple_Factory import Simple_Factory
from .FilterRating import *

class Movies_Getter_Facade:
    def get_movies(self, type : str, rating : str, p_key : int = None, cast_name : str = None, low_r : float = None, high_r : float = None, year : int = None) -> pd.DataFrame:
        simple_factory = Simple_Factory()
        movies_result = simple_factory.movie_getter(type, p_key, cast_name, low_r, high_r, year)
        helper = Filter_Rating()
        movies_result = helper.get_movies_based_on_rating(movies_result, rating)
        return movies_result
