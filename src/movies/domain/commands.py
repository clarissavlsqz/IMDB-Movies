from dataclasses import dataclass
import abc
from .use_cases.Login import *
from .use_cases.Register import *

# Using the Command Design Pattern - It creates a Register and Login Command
# Open Close Princple - New commands can be created

class Command(abc.ABC):
    @abc.abstractmethod
    def execute(self) -> None:
        pass

class RegisterCommand(Command):
    def __init__(self, register : Register, username : str, email : str, g1 : int, g2 : int, g3 : int, repo : AbstractRepository) -> None:
        self._register = register
        self._username = username
        self._email = email
        self._g1 = g1
        self._g2 = g2
        self._g3 = g3
        self._repo = repo

    def execute(self) -> None:
        self._register.register(self._username, self._email, self._g1, self._g2, self._g3, self._repo)

class LoginCommand(Command):
    def __init__(self, login : Login, username : str, email : str, repo : AbstractRepository) -> None:
        self._login = login
        self._username = username
        self._email = email
        self._repo = repo

    def execute(self) -> None:
        self._login.login(self._username, self._email, self._repo)