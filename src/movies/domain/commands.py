from dataclasses import dataclass
import abc
from .model.User import *

class Command(abc.ABC):
    @abc.abstractmethod
    def execute(self) -> None:
        pass

class Register(Command):
    def __init__(self, new_user : User, username : str, email : str, g1 : int, g2 : int, g3 : int, repo : AbstractRepository) -> None:
        self._new_user = new_user
        self._username = username
        self._email = email
        self._g1 = g1
        self._g2 = g2
        self._g3 = g3
        self._repo = repo

    def execute(self) -> None:
        self._new_user.register(self._username, self._email, self._g1, self._g2, self._g3, self._repo)

class Login(Command):
    def __init__(self, r_user : User, username : str, email : str, repo : AbstractRepository) -> None:
        self._r_user = r_user
        self._username = username
        self._email = email
        self._repo = repo

    def execute(self) -> None:
        self._r_user.login(self._username, self._email, self._repo)