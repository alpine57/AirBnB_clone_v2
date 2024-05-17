#!/usr/bin/python3


"""
Distributes archive to webservers
"""
import os
import datetime
from fabric.api import put, run, env, local
env.hosts = ['52.86.124.28', '54.196.40.166']
env.user = 'ubuntu'
env.key_filename = '~/.ssh/id_rsa'


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


def do_deploy(archive_path):
    """
    Distributes archive to webservers
    """
    if not os.path.exists(archive_path):
        return False
    file_name = os.path.basename(archive_path)
    folder_name = file_name.replace(".tgz", "")
    folder_path = "/data/web_static/releases/{}/".format(folder_name)
    try:
        put(archive_path, "/tmp/{}".format(file_name))
        run("mkdir -p {}".format(folder_path))
        run("tar -xzf /tmp/{} -C {}".format(file_name, folder_path))
        run("rm -rf /tmp/{}".format(file_name))
        run("mv {}web_static/* {}".format(folder_path, folder_path))
        run("rm -rf {}web_static".format(folder_path))
        run("rm -rf /data/web_static/current")
        run("ln -s {} /data/web_static/current".format(folder_path))
        print('New version deployed!')
        return (True)
    except Exception:
        return (False)
