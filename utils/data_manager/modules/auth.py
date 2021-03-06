from .. import dm_exceptions
from . import resource

class Auth(resource.Resource):
    table = 'settings_auth'
    name_field = 'username'
    primary_key = 'auth_id'
    search_field = 'username'
    configuration = {
        "fields": {
            "username": {
                "settings": {
                    "type": "text",
                    "require": True,
                    "description": "Username of device",
                    "expected": str
                }
            },
            "password": {
                "settings": {
                    "type": "text",
                    "require": True,
                    "description": "Password of device",
                    "expected": str
                }
            }
        }
    }
