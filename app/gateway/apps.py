from django.apps import AppConfig

class GatewayConfig(AppConfig):
    '''
        this class is used when the app starts up 
    '''
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'gateway'
    
    def ready(self):
        # Import the custom template tags module
        import app.poll_extras
    
    
        
