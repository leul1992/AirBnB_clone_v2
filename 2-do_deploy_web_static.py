#!/usr/bin/python3
from fabric.api import local, cd, put, env, run, sudo
from datetime import datetime
from os import path

env.hosts = ['3.239.74.200', '3.238.233.55']


def do_pack():
    """generates a tgz archive"""
    try:
        date = datetime.now().strftime("%Y%m%d%H%M%S")
        if isdir("versions") is False:
            local("mkdir versions")
        file_name = "versions/web_static_{}.tgz".format(date)
        local("tar -cvzf {} web_static".format(file_name))
        return file_name
    except:
        return None

def do_deploy(archive_path):
    """distributes an archive to web servers"""
    archive_withoutext = path.splitext(path.basename(archive_path))[0]
    if (not path.exists(archive_path)):
        return False
    with cd('/tmp'):
        upload = put(archive_path, archive_withoutext + '.tgz')
    sudo('mkdir -p /data/web_static/releases/{}'.format(archive_withoutext))
    sudo('tar -xzf /tmp/{0}.tgz -C /data/web_static/releases/{0}/'.format(
         archive_withoutext))
    sudo('rm /tmp/{}.tgz'.format(archive_withoutext))
    sudo('mv /data/web_static/releases/{0}/web_static/* \
    /data/web_static/releases/{0}/'.format(archive_withoutext))
    sudo('rm -rf /data/web_static/releases/{}/web_static'.format(
        archive_withoutext))
    sudo('rm -rf /data/web_static/current')
    sudo('ln -s /data/web_static/releases/{} /data/web_static/current'.format(
        archive_withoutext))
    return upload.succeeded
