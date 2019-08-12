import subprocess
import curses
from curses import wrapper
from curses.textpad import Textbox 
import docker
from dtt.colors import Color
from dtt.dock.container import Containers
from dtt.help import help_mode
from dtt.keypad import KeyPad

def get_command(container_id, exec_command):
    return ["docker", "exec", "-i", "-t", container_id, exec_command]

def docker_mode(stdscr):
    client = docker.from_env()
    curses.cbreak()
    containers = Containers(client.containers.list())
    pad = curses.newpad(len(containers.list),curses.COLS)
    pad.keypad(True)
    Color.init()
    while True:
        if len(containers.list) == 0:
            pad.addstr(0, 0, "empty runnning container.", Color.get("RED_WHITE"))
        for i, l in enumerate(containers.list):
            pad.addstr(i, 0, "{}".format(l.id)[:10], Color.get("BLUE"))
            pad.addstr(i, 15, "{}".format(l.name), Color.get("CYAN"))
        pad.move(containers.index, 0);
        pad.refresh(containers.index-(curses.LINES-1), 0, 0, 0, curses.LINES-1, curses.COLS-1)
        c = pad.getch()
        if c in [curses.KEY_ENTER, KeyPad.ENTER]:
            curses.nocbreak() 
            pad.keypad(False)
            pad.clear()
            subprocess.call(["clear"])
            subprocess.call(get_command(containers.current_container.id, "/bin/sh"))
            curses.cbreak() 
            pad.keypad(True) 
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
            pad.keypad(False)
            pad.clear()
            subprocess.call(["clear"])
            subprocess.call(get_command(containers.current_container.id, command))
            curses.cbreak() 
            pad.keypad(True) 
        elif c in [ord('h')]:
            pad.clear()
            wrapper(help_mode)
            curses.cbreak()
        elif c == ord('q'):
            break
    curses.nocbreak()
    pad.keypad(False)
    curses.echo()
    curses.endwin()

