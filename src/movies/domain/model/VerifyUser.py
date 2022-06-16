from adapters.user_repository import *
import db
from service.handlers import *
from domain.model.Login import *

# Single Responsability Principle - Checks that the user's email is in the database and is a user
# Using the Facade Design Pattern - It uses the AbstractRepository Class to verify the existance of the user
class Verify_User_Facade:
    def verify_user(self, _email : str, repo : AbstractRepository) -> None:
        registered_user = repo.get_by_email(_email)
        if registered_user is None:
            raise UserNotFound(f"User is not logged in")
