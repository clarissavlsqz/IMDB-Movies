
from pandas import DataFrame

class Filter_Rating:
    def get_movies_based_on_rating(self, df : DataFrame, rating : str) -> DataFrame:
        if rating == "False":
            df = df.sort_values(by=["rating"])
        else:
            df = df.sort_values(by=["rating"], ascending=False)

        df = df[["movie_title", "rating", "year"]]

        return df.to_dict(orient="records")

