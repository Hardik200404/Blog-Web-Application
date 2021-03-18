from django.apps import AppConfig


class UsersConfig(AppConfig):
    name = 'users'
    def ready(self):
        import users.signals
        #this helps user to send the signal in our signals.py to create a default profile