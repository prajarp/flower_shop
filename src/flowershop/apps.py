from django.apps import AppConfig


class FlowershopConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'flowershop'

    def ready(self):
        import flowershop.signals
            # Ensure signals are imported when the app is ready