from adapters.user_repository import *
import db
from service.handlers import *
from domain.model.Login import *

# Using the Design Patter Facade - It uses the AbstractRepository Class to handle the DB and get the preference key
class Get_PKey_Facade:
    def get_preference_key(self, _email : str, repo : AbstractRepository) -> int:
        registered_user = repo.get_by_email(_email)
        if registered_user is None:
            raise UserNotFound(f"User is not logged in")
        return registered_user.preference_key