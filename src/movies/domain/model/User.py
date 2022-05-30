from __future__ import annotations
from . import KeyGenerator
from adapters.user_repository import *


class User:
    username : str
    email : str
    preference_key : int

    def register(self, _username : str, _email : str, _first_genre : int, _second_genre : int, _third_genre : int, repo : AbstractRepository) -> None: 
        if repo.get_by_username(_username) is None:
            self.username = _username
            
        self.email = _email
        p_key = KeyGenerator.original_key_generator(_first_genre, _second_genre, _third_genre)
        self.preference_key = p_key
        repo.add(self) # insert to database

    def login(self, _username : str, _email : str, repo : AbstractRepository) -> bool:
        registered_user = repo.get(_username, _email)   # check query and see if it returns an object
        if registered_user is not None: 
            return True
        else:
            return False