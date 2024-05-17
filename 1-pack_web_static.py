#!/usr/bin/python3

"""Module generates archive from the contents of web_static folder"""

import datetime
import os
from fabric.api import local


def do_pack():
    """
    Zips files in web_static folder
    """
    t = datetime.datetime.now().strftime('%Y%m%d%H%M%S')
    local('mkdir -p ./versions')
    local(f'tar -cvzf versions/web_static_{t}.tgz web_static')
    if os.path.exists(f'versions/web_static_{t}.tgz'):
        return (f'versions/web_static_{t}.tgz')
    else:
        return (None)
