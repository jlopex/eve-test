# vim: ai ts=4 sts=4 et sw=4


# MongoDB settings
MONGO_HOST = 'localhost'
MONGO_PORT = 27017
MONGO_USERNAME = 'user'
MONGO_PASSWORD = 'user'
MONGO_DBNAME = 'apitest'

#DEBUG = True

# Enable reads (GET), inserts (POST) and DELETE for resources/collections
# (if you omit this line, the API will default to ['GET'] and provide
# read-only access to the endpoint).
RESOURCE_METHODS = ['GET', 'POST', 'DELETE']

# Enable reads (GET), edits (PATCH), replacements (PUT) and deletes of
# individual items  (defaults to read-only item access).
ITEM_METHODS = ['GET', 'PATCH', 'PUT', 'DELETE']

schema = {
    # Schema definition, based on Cerberus grammar. Check the Cerberus project
    # (https://github.com/nicolaiarocci/cerberus) for details.
    'username': {
        'type': 'string',
        'minlength': 1,
        'maxlength': 256,
    },
    'password': {
        'type': 'string',
        'minlength': 1,
        'maxlength': 256,
    },
    'filename': {
        'type': 'string',
        'minlength': 1,
        'maxlength': 256,
    },
    'url': {
        'type': 'string',
        'minlength': 5,
        'maxlength': 1024,
        'required': True,
        'unique': True,
    },
    'query': {
        'type': 'dict',
        'required': True,
    },
    'store_path': {
        'type': 'string',
        'minlength': 3,
        'maxlength': 256,
        'required': True,
    },
    'provider': {
        'type': 'string',
        'minlength': 1,
        'maxlength': 64,
        'required': True,
    },
    'status': {
        'type': 'string',
        'allowed': ["PENDING", "DOWNLOADING", "DOWNLOADED", "FAILED"],
        'required': True,
    },
    'notify_list': {
        'type': 'list',
        'items': [{'type': 'string'}],
    }
}

downloads = {
    # We choose to override global cache-control directives for this resource.
    'cache_control': 'max-age=10,must-revalidate',
    'cache_expires': 10,

    # most global settings can be overridden at resource level
    #'resource_methods': ['GET', 'POST'],

    'schema': schema
}

DOMAIN = {
	'downloads': downloads,
}


