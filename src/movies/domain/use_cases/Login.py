from adapters.user_repository import *
from service.handlers import *
from utils.validate_email import *

# Single Responsability Principle - This class is only used to login the user

class Login:
    def login(self, _username : str, _email : str, repo : AbstractRepository) -> None:
        registered_user = repo.get(_username, _email)   # check query and see if it returns an object
        if registered_user is None: 
            raise UserNotFound(f"User with username: {_username} and email: {_email} was not found in our database")