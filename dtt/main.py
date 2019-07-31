#!/usr/bin/env python
# -*- coding: utf-8 -*-
import curses
import subprocess
from help import help_mode
from curses import wrapper
from colors import Color

from kubernetes import client, config

def docker_mode(stdscr):
    import docker
    from dock.container import Containers
    client = docker.from_env()
    curses.cbreak()
    stdscr.keypad(True)
    Color.init()
    containers = Containers(client.containers.list())
    while True:
        if len(containers.list) == 0:
            stdscr.addstr(0, 0, "empty runnning container.", Color.get("RED_WHITE"))
        for i, l in enumerate(containers.list):
            stdscr.addstr(i, 0, "{}".format(l.id)[:10], Color.get("BLUE"))
            stdscr.addstr(i, 15, "{}".format(l.name), Color.get("CYAN"))
        stdscr.move(containers.index, 0);
        c = stdscr.getch()
        if c == 10:
            curses.nocbreak() 
            stdscr.keypad(False)
            stdscr.clear()
            subprocess.call(["clear"])
            subprocess.call(["docker", "exec", "-i", "-t", containers.current_container.id, "/bin/sh"])
            curses.cbreak() 
            stdscr.keypad(True) 
        elif c == ord('j'):
            containers.add_index()
        elif c == ord('k'):
            containers.sub_index()
        elif c == ord('h'):
            stdscr.clear()
            wrapper(help_mode)
            curses.cbreak()
        elif c == ord('q'):
            break
    curses.nocbreak()
    stdscr.keypad(False)
    curses.echo()
    curses.endwin()

def kubectl_mode(stdscr):
    from kubectl.pod import Pods
    curses.cbreak()
    stdscr.keypad(True)
    Color.init()
    pods = Pods(get_kube_pods('argo'))
    while True:
        if len(pods.list) == 0:
            stdscr.addstr(0, 0, "empty runnning pods.", Color.get("RED_WHITE"))
        for i, l in enumerate(pods.list):
            stdscr.addstr(i, 0, "{}".format(l.metadata.name), Color.get("BLUE"))
        stdscr.move(pods.index, 0);
        c = stdscr.getch()
        if c == 10:
            curses.nocbreak() 
            stdscr.keypad(False)
            stdscr.clear()
            subprocess.call(["clear"])
            subprocess.call(["kubectl", "exec", "-i", "-t", "--namespace", "argo", pods.current_pod.metadata.name, "/bin/sh"])
            curses.cbreak() 
            stdscr.keypad(True) 
        elif c == ord('j'):
            pods.add_index()
        elif c == ord('k'):
            pods.sub_index()
        elif c == ord('h'):
            stdscr.clear()
            wrapper(help_mode)
            curses.cbreak()
        elif c == ord('q'):
            break
    curses.nocbreak()
    stdscr.keypad(False)
    curses.echo()
    curses.endwin()

def get_kube_pods(namespace):
    config.load_kube_config()
    v1 = client.CoreV1Api()
    return v1.list_namespaced_pod(namespace, watch=False)

from docopt import docopt

__doc__ = """{f}
Usage:
    {f}
    {f} -k | --kubectl
    {f} -h | --help
Options:
    -k --kubectl             kubectl mode
    -h --help                Show this screen and exit.
""".format(f='dtt')


def main():
    args = docopt(__doc__)
    if args['--kubectl']:
        wrapper(kubectl_mode)
    elif args['--help']:
        pass
    else:
        wrapper(docker_mode)

if __name__ == '__main__':
    main()
