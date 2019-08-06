import subprocess
import curses
from colors import Color
from curses import wrapper
from help import help_mode
from curses.textpad import Textbox 
from keypad import KeyPad

def mode_gen(item_name, items, get_command):
    def f(stdscr):
        curses.cbreak()
        pad = curses.newpad(len(items.list),curses.COLS)
        pad.keypad(True)
        Color.init()
        while True:
            if len(items.list) == 0:
                pad.addstr(0, 0, "empty runnning {}.".format(item_name), Color.get("RED_WHITE"))
            for i, l in enumerate(items.list):
                pad.addstr(i, 0, "{}".format(l.id)[:10], Color.get("BLUE"))
                pad.addstr(i, 15, "{}".format(l.name), Color.get("CYAN"))
            pad.move(items.index, 0);
            pad.refresh(items.index-(curses.LINES-1), 0, 0, 0, curses.LINES-1, curses.COLS-1)
            c = pad.getch()
            if c in [curses.KEY_ENTER, KeyPad.ENTER]:
                curses.nocbreak() 
                pad.keypad(False)
                pad.clear()
                subprocess.call(["clear"])
                subprocess.call(get_command(items.current_item.id, "/bin/sh"))
                curses.cbreak() 
                pad.keypad(True) 
            elif c in [ord('j'), curses.KEY_DOWN]:
                items.add_index()
            elif c in [ord('k'), curses.KEY_UP]:
                items.sub_index()
            elif c == ord('X'):
                win = curses.newwin(1, curses.COLS-1, curses.LINES-1, 0)
                box = Textbox(win)
                box.edit()
                command = box.gather().rstrip()
                curses.nocbreak() 
                pad.keypad(False)
                pad.clear()
                subprocess.call(["clear"])
                subprocess.call(get_command(items.current_item.id, command))
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
    return f


class Items:
    def __init__(self, items, namespace=None):
        self._index = 0
        self._items = items
    @property
    def index(self):
        return self._index
    @property
    def current_item(self):
        return self._items[self._index]
    @property
    def list(self):
        return self._items
    def set_index(self, index):
        self._index = index
    def add_index(self):
        if self._index + 1 < len(self._items):
            self._index += 1
    def sub_index(self):
        if 0 <= self._index - 1:
            self._index -= 1
    def get_command(self):
        if 0 <= self._index - 1:
            self._index -= 1
