#!/usr/bin/python3
"""Distributes the content of the archive to the web servers"""
from fabric.api import *
from datetime import datetime
import os

env.hosts = ['<IP web-01>', 'IP web-02']


# def do_pack():
#     """pack function"""
#     try:
#         if not os.path.exists('versions'):
#             os.mkdir('versions')
#         date_str = datetime.now().strftime('%Y%m%d%H%M%S')
#         file_path = 'versions/web_static_{}.tgz'.format(date_str)
#         local('tar -cvzf {} web_static'.format(file_path))
#         return file_path
#     except:
#         return None


def do_deploy(archive_path):
    """Deploy function"""
    try:
        if not os.path.exists(archive_path):
            return False
        put(archive_path, '/tmp/')
        archive_folder = archive_path.split('.')[0].split('/')[-1]
        sudo('mkdir -p /data/web_static/releases/{}'.format(archive_folder))
        sudo(f'tar -xzf /tmp/{archive_folder}.tgz -C /data/web_static/'
             f'releases/{archive_folder}/')
        sudo(f'rm /tmp/{archive_folder}.tgz')
        sudo(f'mv /data/web_static/releases/{archive_folder}/web_static/*'
             f' /data/web_static/releases/{archive_folder}')
        sudo(f'rm -rf /data/web_static/releases/{archive_folder}/web_static/')
        sudo('rm -rf /data/web_static/current')
        sudo(f'ln -s /data/web_static/releases/{archive_folder} '
             f'/data/web_static/current')
        print('New version deployed!')
        return True
    except FileNotFoundError:
        return False
