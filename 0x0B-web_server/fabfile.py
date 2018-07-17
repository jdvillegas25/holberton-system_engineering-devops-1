#!/usr/bin/python3
'''
Fabric file for transferring a file to a remote server from local machine
'''

from fabric.api import *
env.user = 'ubuntu'
env.key_filename = '~/.ssh/holberton'


def pack():
    '''
    Packages the current directory into a .tar.gz archive
    '''

    local("tar --exclude='*.tar.gz' -zcvf holbertonwebapp.tar.gz .")


def deploy():
    '''
    Deploys the archive onto the remote server in /tmp/,
    creates a holbertonwebapp folder, and extracts the
    archive contents into this directory
    '''

    put("./holbertonwebapp.tar.gz", "/tmp/holbertonwebapp.tar.gz")
    run("mkdir /tmp/holbertonwebapp/")
    run("tar -zxvf /tmp/holbertonwebapp.tar.gz -C /tmp/holbertonwebapp/")


def clean():
    '''
    Removes the archive from the local machine
    '''

    local("rm holbertonwebapp.tar.gz")
