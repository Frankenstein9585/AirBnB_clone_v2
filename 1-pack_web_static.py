#!/usr/bin/python3
"""Generates a .tgz archive from web_static"""
from fabric.api import local
from datetime import datetime
import os


def do_pack():
    """pack function"""
    try:
        if not os.path.exists('versions'):
            os.mkdir('versions')
        date_str = datetime.now().strftime('%Y%m%d%H%M%S')
        file_path = 'versions/web_static_{}.tgz'.format(date_str)
        local('tar -cvzf {} web_static'.format(file_path))
        return file_path
    except:
        return None
