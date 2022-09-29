#!/usr/bin/env python3
"""fabric script"""
from fabric.api import local
from datetime import datetime

def do_pack():
    """script generates .tgz archive form web_static content"""
    date = datetime.now().strftime('%Y%m%d%H%M%S')
    file_path = 'versions/web_static_{}.tgz'.format(date)
    local('mkdir /versions/')
    gen = local('tar -cvzf {} web_static'.format(file_path))
    if gen.succeeded:
        return file_path
