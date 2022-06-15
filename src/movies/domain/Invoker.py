from domain.commands import Command

class Invoker:
    _user = None
    
    def set_action(self, command : Command):
        self._user = command
# TODO: change name of function to a more explicit one
    def set_user(self) -> None:
        if isinstance(self._user, Command):
            self._user.execute()