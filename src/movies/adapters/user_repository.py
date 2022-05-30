import abc
from .models import User

class AbstractRepository(abc.ABC):
    def __init__(self) -> None:
        self.seen = set()

    def add(self, user: User):
        self._add(user)
        self.seen.add(user)

    def get(self, username, email) -> User:
        user = self._get(username, email)
        if user:
            self.seen.add(user)
        return user

    def get_by_username(self, username) -> User:
        user = self._get_by_username(username)
        if user:
            self.seen.add(user)
        return user

    def get_by_email(self, email) -> User:
        user = self._get_by_email(email)
        if user:
            self.seen.add(user)
        return user

    @abc.abstractmethod
    def _add(self, user: User):
        raise NotImplementedError

    @abc.abstractmethod
    def _get(self, username, email) -> User:
        raise NotImplementedError

    @abc.abstractmethod
    def _get_by_username(self, username) -> User:
        raise NotImplementedError
  
    @abc.abstractmethod
    def _get_by_email(self, email) -> User:
        raise NotImplementedError
    

class SqlAlchemyRepository(AbstractRepository):
    def __init__(self, session):
        super().__init__()
        self.session = session

    def _add(self, user):
        self.session.add(user)
        self.session.commit()

    def _get(self, username, email):
        return self.session.query(User).filter_by(username=username, email = email).first()

    def _get_by_username(self, username):
        return self.session.query(User).filter_by(username=username).first()

    def _get_by_email(self, email):
        return self.session.query(User).filter_by(email = email).first()
