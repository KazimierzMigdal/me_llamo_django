from django.apps import AppConfig


class MemoCardConfig(AppConfig):
    name = 'memo_card'

    def ready(self):
        import users.signals
