#!/usr/bin/env python
# -*- coding: utf-8 -*-
import docker
import curses
import subprocess

from help import help_mode

from curses import wrapper
client = docker.from_env()

from container import Containers
from colors import Color

def ex(stdscr):
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

def main():
    wrapper(ex)

if __name__ == '__main__':
    main()
