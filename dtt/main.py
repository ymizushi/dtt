#!/usr/bin/env python
import docker
import curses
import subprocess

from curses import wrapper
client = docker.from_env()

from container import Containers

def ex(stdscr):
    curses.cbreak()
    stdscr.keypad(True)
    curses.init_pair(1, curses.COLOR_RED, curses.COLOR_WHITE)
    containers = Containers(client.containers.list())
    while True:
        for i, l in enumerate(containers.list):
            stdscr.addstr(i, 0, "{}".format(l.id)[:10], curses.color_pair(1))
            stdscr.addstr(i, 15, "{}".format(l.name))
        stdscr.move(containers.index, 0);
        c = stdscr.getch()
        if c == 10:
            curses.nocbreak()
            stdscr.keypad(False)
            stdscr.clear()
            subprocess.call(["clear"])
            subprocess.call(["docker", "exec", "-i", "-t", containers.current_container.id, "/bin/sh"])
            curses.cbreak()
        elif c == ord('j'):
            containers.add_index()
        elif c == ord('k'):
            containers.sub_index()
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
