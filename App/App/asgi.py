import os

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'App.settings')

application = get_asgi_application()




# посмотреть как делать авторизацию и регистрацию через rest
# авторизация, админ панель,  придумать как привязать к пользователю инфу с бд
