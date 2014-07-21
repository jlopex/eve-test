# MongoDB settings
MONGO_HOST = 'localhost'
MONGO_PORT = 27017
MONGO_USERNAME = 'user'
MONGO_PASSWORD = 'user'
MONGO_DBNAME = 'apitest'

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
    'filename': {
	'type': 'string',
	'minlength': 3,
	'maxlength': 256
    },
    'fasplink': {
        'type': 'string',
        'minlength': 5,
        'maxlength': 1024,
        'required': True,
        # talk about hard constraints! For the purpose of the demo
        # 'lastname' is an API entry-point, so we need it to be unique.
        'unique': True,
    },
    'provider': {
        'type': 'string',
        'minlength': 1,
        'maxlength': 64,
        'required': True,
    },
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


