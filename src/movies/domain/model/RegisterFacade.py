import db
from adapters import user_repository
from domain.Invoker import Invoker
from domain.commands import RegisterCommand
from domain.model.Register import Register

# Using the Facade Design Pattern - All the dependencies are used in the Facade instead of using them directly from the route

class Register_Facade:
    def register_user(self, user_username : str, user_email : str, first_genre : str, second_genre : str, third_genre : str):
        new_user = Invoker()
        register = Register()
        repo = user_repository.SqlAlchemyRepository(db.session)
        new_user.set_action(RegisterCommand(register, user_username, user_email, first_genre, second_genre, third_genre, repo))
        new_user.invoke()