import subprocess
import curses
from dtt.kubectl.client import Client
from dtt.kubectl.pod import Pods
from dtt.colors import Color
from dtt.help import help_mode
from dtt.config import Config
from dtt.keypad import KeyPad

def get_command(pod_name, namespace, exec_command):
    return ["kubectl", "exec", "-i", "-t", "--namespace", namespace, pod_name, exec_command]

def kubectl_mode(stdscr):
    curses.cbreak()
    Color.init()
    try:
        namespace = Config()["default"]["kubectl"]["namespace"]
    except:
        namespace = None
    pods = Pods(get_kube_pods(namespace))
    pad = curses.newpad(len(pods.list),curses.COLS)
    pad.keypad(True)
    while True:
        if len(pods.list) == 0:
            pad.addstr(0, 0, "empty runnning pods.", Color.get("RED_WHITE"))
        for i, l in enumerate(pods.list):
            pad.addstr(i, 0, "{}".format(l.metadata.name), Color.get("CYAN"))
        pad.move(pods.index, 0);
        pad.refresh(pods.index-(curses.LINES-1), 0, 0, 0, curses.LINES-1, curses.COLS-1)
        c = pad.getch()
        if c in [curses.KEY_ENTER, KeyPad.ENTER]:
            curses.nocbreak() 
            pad.keypad(False)
            pad.clear()
            subprocess.call(["clear"])
            exec_command = "/bin/sh"
            subprocess.call(get_command(pods.current_pod.metadata.name, pods.current_pod.metadata.namespace, exec_command))
            curses.cbreak() 
            pad.keypad(True) 
        elif c in [ord('j'), curses.KEY_DOWN]:
            pods.add_index()
        elif c in [ord('k'), curses.KEY_UP]:
            pods.sub_index()
        elif c == ord('h'):
            pad.clear()
            wrapper(help_mode)
            curses.cbreak()
        elif c == ord('X'):
            win = curses.newwin(1, curses.COLS-1, curses.LINES-1, 0)
            box = Textbox(win)
            box.edit()
            command = box.gather().rstrip()

            curses.nocbreak() 
            pad.keypad(False)
            pad.clear()
            subprocess.call(["clear"])
            subprocess.call(get_command(pods.current_pod.metadata.name, pods.current_pod.metadata.namespace, command))
            curses.cbreak() 
            pad.keypad(True) 
        elif c == ord('q'):
            break
    curses.nocbreak()
    pad.keypad(False)
    curses.echo()
    curses.endwin()

def get_kube_pods(namespace=None):
    Client.load_config()
    client = Client()
    if namespace:
        return client.list_namespaced_pod(namespace, watch=False)
    else:
        return client.list_pod_for_all_namespaces(watch=False)
