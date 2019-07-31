import subprocess
import curses
from colors import Color
from curses import wrapper
import docker
from dock.container import Containers
from help import help_mode

def get_command(container_id, exec_command):
    return ["docker", "exec", "-i", "-t", container_id, exec_command]

def docker_mode(stdscr):
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
            subprocess.call(get_command(containers.current_container.id, "/bin/sh"))
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

