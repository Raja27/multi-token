# Multi token for django rest framework

##Installation
##------------
pip install django-multi-token

##Settings File
##-------------

INSTALLED_APPS = [
    ...
    'tokens'
    ...
]


```REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        # 'rest_framework.authentication.TokenAuthentication',
        'tokens.models.MultiTokenAuthentication',
    )
}```
