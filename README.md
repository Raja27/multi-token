# Multi token for django rest framework
> Using this app user can maintain seperate auth token for each device. Logout form one device will not logout other device.
So multiple login is possiable using this app.
## Installation
```pip install django-multi-token```

## Settings File
```
INSTALLED_APPS = [
    ...
    'tokens'
    ...
]
```


```
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        # 'rest_framework.authentication.TokenAuthentication',
        'tokens.models.MultiTokenAuthentication',
    )
}
```
