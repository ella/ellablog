# load base configuration for whole app
from ellablog.settings.base import *

# load some dev env configuration options
from ellablog.settings.config import *

# try to import some settings from /etc/
import sys
sys.path.insert(0, '/etc/ella')
try:
    from ellablog_config import *
except ImportError:
    pass
del sys.path[0]

# load any settings for local development
try:
    from ellablog.settings.local import *
except ImportError:
    pass
