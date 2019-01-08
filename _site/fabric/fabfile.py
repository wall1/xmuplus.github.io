#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import print_function, absolute_import, with_statement

import os
import sys
import ftplib
import getpass
from fabric.api import env, local, task, settings
from fabric.colors import blue, red
import fabric.contrib.project as project
from simiki import config

# XXX must run fab in root path of wiki
configs = config.parse_config('_config.yml')

env.colorize_errors = True
SUPPORTED_DEPLOY_TYPES = ('rsync', 'git', 'ftp')


def do_exit(msg):
    print(red(msg))
    print(blue('Exit!'))
    sys.exit()


def get_rsync_configs():
    if 'deploy' in configs:
        for item in configs['deploy']:
            if item['type'] == 'rsync':
                return item
    return None

# cannot put this block in deploy_rsync() for env.hosts
rsync_configs = get_rsync_configs()
if rsync_configs:
    env.user = rsync_configs.get('user', 'root')
    # Remote host and username
    if 'host' not in rsync_configs:
        do_exit('Warning: rsync host not set in _config.yml!')
    env.hosts = [rsync_configs['host'],]

    # Local output path
    env.local_output = os.path.join(
        os.path.abspath(os.path.dirname(__file__)),
        configs['destination'])

    # Remote path to deploy output
    if 'dir' not in rsync_configs:
        do_exit('Warning: rsync dir not set in _config.yml!')
    env.remote_output = rsync_configs['dir']

    # Other options
    env.port = rsync_configs.get('port')
    env.rsync_delete = rsync_configs.get('delete', False)


def deploy_rsync(deploy_configs):
    '''for rsync'''
    project.rsync_project(
        local_dir=env.local_output.rstrip("/")+"/",
        remote_dir=env.remote_output.rstrip("/")+"/",
        delete=env.rsync_delete
    )




@task
def deploy(type=None):
    '''
    run deploy:
        $ fab deploy

    '''
    if 'deploy' not in configs or not isinstance(configs['deploy'], list):
        do_exit('Warning: deploy not set right in _config.yml')
    if type and type not in SUPPORTED_DEPLOY_TYPES:
        do_exit('Warning: supported deploy type: {0}'
                .format(', '.join(SUPPORTED_DEPLOY_TYPES)))

    deploy_configs = configs['deploy']

    done = False

    for deploy_item in deploy_configs:
        deploy_type = deploy_item.pop('type')
        if type and deploy_type != type:
            continue
        func_name = 'deploy_{0}'.format(deploy_type)
        func = globals().get(func_name)
        if not func:
            do_exit('Warning: not supprt {0} deploy method'.format(deploy_type))
        func(deploy_item)
        done = True

    if not done:
        if type:
            do_exit('Warning: specific deploy type not configured yet')
        else:
            print(blue('do nothing...'))
