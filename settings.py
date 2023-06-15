import os


DBCreds = {
    'HOST': os.environ.get('HOST', 'localhost'),
    'USER': os.environ.get('USER', 'myuser'),
    'PORT': os.environ.get('PORT', 3306),
    'PASSWORD': os.environ.get('PASSWORD', 'mypassword'),
    'DB':  os.environ.get('DATABASE', 'users_db')
}
