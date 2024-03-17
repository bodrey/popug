import sys
from jsonschema import validate

def meow(string = 'Meow!'):
    print('', file=sys.stderr)
    print(string, file=sys.stderr)
    print('', file=sys.stderr)

    print('')
    print(string)
    print('')

schema_task_to_auth = {
    "$schema": "http://json-schema.org/draft-07/schema#",
    "type" : "object",
    "properties": {
        "token": { "type": ["string", "null"] },
    },
    "required": ["token"]
}

schema_auth_to_task = {
    "$schema": "http://json-schema.org/draft-07/schema#",
    "type" : "object",
    "properties": {
        "user_id": { "type": ["string", "null"] },
    },
    "required": ["user_id"]
}
