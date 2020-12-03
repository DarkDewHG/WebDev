from django.apps import AppConfig


class UsersblockConfig(AppConfig):
    name = 'usersblock'

    def ready(self):
        import usersblock.signals