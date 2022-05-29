import validate_email

class User:
    username : str
    email : str
    preference_key : int

    def set_username(self, _username) -> None:
        self.username = _username

    def set_email(self, _email) -> bool:
        if validate_email.check(_email):
            self.email = _email
            return True;
        else:
            return False;

    def set_preference_key(self, key) -> None:
        self.preference_key = key