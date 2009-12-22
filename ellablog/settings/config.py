from tempfile import gettempdir
from os.path import join, dirname

import ellablog

DEBUG = True
TEMPLATE_DEBUG = DEBUG

# database settings
DATABASE_ENGINE = 'sqlite3'
DATABASE_NAME = join(gettempdir(), 'ellablog.db')

# Make this unique, and don't share it with anybody.
SECRET_KEY = '1#h7o0k$ea%ciox$$p&@(r&1eokb*mvk(n(v9!wb11bt(^4$ns'

CACHE_BACKEND = 'dummy://'

