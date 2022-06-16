from domain.commands import Command
# We use this class to invoke the command
class Invoker:
    _user = None
    
    def set_action(self, command : Command):
        self._user = command

    def invoke(self) -> None:
        if isinstance(self._user, Command):
            self._user.execute()