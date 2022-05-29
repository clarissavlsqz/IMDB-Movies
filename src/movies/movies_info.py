import pandas as pd

def getMovieRecs(rating : bool, preference_key : int) -> pd.DataFrame:
    movies_result = pd.read_csv("movie_results.csv")
    movies_based_on_pref_key = movies_result[movies_result['preference_key'] == preference_key]
    if rating:
        movies_based_on_pref_key = movies_based_on_pref_key.sort_values(by=["rating"], ascending=False).head(10)
    else:
        movies_based_on_pref_key = movies_based_on_pref_key.sort_values(by=["rating"]).head(10)
    return movies_based_on_pref_key

def getMoviesByStar(name : str) -> pd.DataFrame:
    movies_result = pd.read_csv("movie_results.csv")
    movies_based_on_star = movies_result[movies_result.str.contains(name)]
    return movies_based_on_star

def getMoviesByRating(low : float, high : float) -> pd.DataFrame:
    movies_result = pd.read_csv("movie_results.csv")
    movies_based_on_rating = movies_result[movies_result["rating"] >= low & movies_result["rating"] <= high]
    return movies_based_on_rating

def getMoviesByYear(year : int) -> pd.DataFrame:
    movies_result = pd.read_csv("movie_results.csv")
    movies_based_on_year = movies_result[movies_result["year"] == year]
    return movies_based_on_year
