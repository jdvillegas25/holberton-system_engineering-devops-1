#!/usr/bin/python3
'''
Fabric file for transferring a file to a remote server from local machine
'''

from fabric.api import *
env.user = 'ubuntu'
env.key_filename = '~/.ssh/holberton'

def pack():
    local("tar --exclude='*.tar.gz' -zcvf holbertonwebapp.tar.gz .")


def deploy():
    put("./holbertonwebapp.tar.gz", "/tmp/holbertonwebapp.tar.gz")
    run("mkdir /tmp/holbertonwebapp")
    run("tar -zxvf /tmp/holbertonwebapp.tar.gz -C /tmp/holbertonwebapp/")

def clean():
    local("rm ./holbertonwebapp.tar.gz")
