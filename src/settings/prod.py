# This file is only used if you use `make publish` or
# explicitly specify it as your config file.

import os
import sys

sys.path.append(os.curdir)
from .dev import *  # noqa: F403

# If your site is available via HTTPS, make sure SITE_URL begins with https://
SITE_URL = "https://x8lucas8x.com"
