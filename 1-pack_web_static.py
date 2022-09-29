#!/usr/bin/env python3
"""fabric script"""
from fabric.api import local
from datetime import datetime

def do_pack():
    """script generates .tgz archive form web_static content"""
    date = datetime.now().strftime('%Y%m%d%H%M%S')
    file_name = 'versions/web_static_{}.tgz'.format(date)
    local('mkdir -p versions/')
    gen = local('tar -cvf {} web_static'.format(file_name))
    if (gen.succeeded):
        return file_name
    else:
        return None
