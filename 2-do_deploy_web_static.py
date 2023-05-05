#!/usr/bin/python3
"""Distributes the content of the archive to the web servers"""
from fabric.api import sudo, put, env
import os

env.hosts = ['ubuntu@100.26.216.194']


def do_deploy(archive_path):
    """Deploy function"""
    try:
        if not os.path.exists(archive_path):
            return False
        put(archive_path, '/tmp/')
        archive_folder = archive_path.split('.')[0].split('/')[-1]
        sudo('mkdir -p /data/web_static/releases/{}'.format(archive_folder))
        sudo(f'tar -xzf /tmp/{archive_folder}.tgz -C /data/web_static/releases/{archive_folder}/')
        sudo(f'rm /tmp/{archive_folder}.tgz')
        sudo(f'mv /data/web_static/releases/{archive_folder}/web_static/* /data/web_static/releases/{archive_folder}')
        sudo(f'rm -rf /data/web_static/releases/{archive_folder}/web_static/')
        sudo('rm -rf /data/web_static/current')
        sudo(f'ln -s /data/web_static/releases/{archive_folder} /data/web_static/current')
        return True
    except:
        return False
