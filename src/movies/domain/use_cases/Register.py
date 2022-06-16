from utils.KeyGenerator import KeyGenerator
from adapters.user_repository import *
from service.handlers import *
from utils.validate_email import *
from adapters.models import User

# Single Responsability Principle - This class is only used to register the user

class Register:

    def register(self, username : str, email : str, first_genre : int, second_genre : int, third_genre : int, repo : AbstractRepository) -> None: 
        if repo.get_by_username(username) is not None:
            raise UsedUsername(f"Username {username} repeated, please enter another one")
            
        if check(email):
            if repo.get_by_email(email) is not None:
                raise UsedEmail(f"Email {email} is already used for another user, please enter an used email")               
        else:
            raise InvalidEmail(f"{email} is not a valid email address")
        
        p_key = KeyGenerator.original_key_generator(first_genre, second_genre, third_genre)
        
        new_user = User(p_key, username, email)
        repo.add(new_user) # insert to database