import pandas as pd
from domain.model.Movies_Getter import *

# Using the simple Factory Design Pattern - We generate the DataFrame speicifc to the endpoint called

class Simple_Factory:
    def movie_getter(self, type : str, p_key : int, cast_name : str, low_r : float, high_r : float, year : int) -> pd.DataFrame:
        if type == "recommendation":
            result = Movies_Recommendation()
            return result.get_movies(p_key)
        elif type == "star cast":
            result = Movies_Cast()
            return result.get_movies(cast_name)
        elif type == "rating":
            result = Movies_Rating()
            return result.get_movies(low_r, high_r)
        elif type == "year":
            result = Movies_Year()
            return result.get_movies(year)


