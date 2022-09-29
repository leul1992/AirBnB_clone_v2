#!/usr/bin/env python3
"""fabric script"""
from fabric.api import local
from datetime import datetime

def do_pack():
    """script generates .tgz archive form web_static content"""
    date = datetime.now().strftime('%Y%m%d%H%M%S')
    file_path = f'versions/web_static_{date}'
    local('mkdir /versions/')
    gen = local(f'tar -cvzf {file_path} web_static')
    if gen.succeeded):
        return file_path
