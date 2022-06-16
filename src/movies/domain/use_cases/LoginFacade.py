import service.db as db
from adapters import user_repository
from domain.Invoker import Invoker
from domain.commands import LoginCommand
from domain.use_cases.Login import Login

# Using the Facade Design Pattern - All the dependencies are used in the Facade instead of using them directly from the route

class Login_Facade:
    def login_user(self, user_username : str, user_email : str):
        registered_user = Invoker()
        login = Login()
        repo = user_repository.SqlAlchemyRepository(db.session)
        registered_user.set_action(LoginCommand(login, user_username, user_email, repo))
        registered_user.invoke()