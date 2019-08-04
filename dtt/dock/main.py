import subprocess
import curses
from colors import Color
from curses import wrapper
import docker
from dock.container import Containers
from help import help_mode
from curses.textpad import Textbox 
from keypad import KeyPad


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
        if c in [curses.KEY_ENTER, KeyPad.ENTER]:
            curses.nocbreak() 
            stdscr.keypad(False)
            stdscr.clear()
            subprocess.call(["clear"])
            subprocess.call(get_command(containers.current_container.id, "/bin/sh"))
            curses.cbreak() 
            stdscr.keypad(True) 
        elif c in [ord('j'), curses.KEY_DOWN]:
            containers.add_index()
        elif c in [ord('k'), curses.KEY_UP]:
            containers.sub_index()
        elif c == ord('X'):
            win = curses.newwin(1, curses.COLS-1, curses.LINES-1, 0)
            box = Textbox(win)
            box.edit()
            command = box.gather().rstrip()

            curses.nocbreak() 
            stdscr.keypad(False)
            stdscr.clear()
            subprocess.call(["clear"])
            subprocess.call(get_command(containers.current_container.id, command))
            curses.cbreak() 
            stdscr.keypad(True) 
        elif c in [ord('h')]:
            stdscr.clear()
            wrapper(help_mode)
            curses.cbreak()
        elif c == ord('q'):
            break
    curses.nocbreak()
    stdscr.keypad(False)
    curses.echo()
    curses.endwin()

