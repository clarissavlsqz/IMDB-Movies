import user
import register_login
import movies_info

def main():
    new_user = user()
    preference_key = register_login.welcome_message(new_user)
    df = movies_info.getMovieRecs(False, preference_key)
    print(df.to_string)