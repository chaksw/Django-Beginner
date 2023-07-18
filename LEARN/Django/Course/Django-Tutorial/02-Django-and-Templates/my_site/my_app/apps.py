from django.apps import AppConfig

# the class is automatically create with 'django-admin start app'
# and used to be referred as 'INSTALLED_APPS' in 'setting.py'
class MyAppConfig(AppConfig):
    name = 'my_app'


# in case any changes in app, use 'py -3.11 .\manage.py makemigrations my_app' to apply the changes
