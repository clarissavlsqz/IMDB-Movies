import abc
from typing import Set
import others.client as model # es la clase User
import models as orm

class AbstractRepository(abc.ABC):
    def __init__(self) -> None:
        self.seen = set()

    def add(self, user: model.User):
        self._add(user)
        self.seen.add(user)

    def get(self, username, email) -> model.User:
        user = self._get(username, email)
        if user:
            self.seen.add(user)
        return user

    def get_by_username(self, username) -> model.User:
        user = self._get_by_username(username)
        if user:
            self.seen.add(user)
        return user

    def get_by_email(self, email) -> model.User:
        user = self._get_by_email(email)
        if user:
            self.seen.add(user)
        return user

    @abc.abstractmethod
    def _add(self, user: model.User):
        raise NotImplementedError

    @abc.abstractmethod
    def _get(self, username, email) -> model.User:
        raise NotImplementedError

    @abc.abstractmethod
    def _get_by_username(self, username) -> model.User:
        raise NotImplementedError
  
    @abc.abstractmethod
    def _get_by_email(self, email) -> model.User:
        raise NotImplementedError
    

class SqlAlchemyRepository(AbstractRepository):
    def __init__(self, session):
        super().__init__()
        self.session = session

    def _add(self, user):
        self.session.add(user)

    def _get(self, username, email):
        return self.session.query(model.User).filter_by(username=username, email = email).first()

    def _get_by_username(self, username):
        return (
            self.session.query(model.User)
            .filter_by(username=username)
            .first()
        )

    def _get_by_email(self, email):
        return (
            self.session.query(model.User)
            .filter_by(email = email)
            .first()
        )
