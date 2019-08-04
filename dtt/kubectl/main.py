import subprocess
import curses
from colors import Color
from help import help_mode
from config import Config
from kubectl.client import Client
from keypad import KeyPad

def get_command(pod_name, namespace, exec_command):
    return ["kubectl", "exec", "-i", "-t", "--namespace", namespace, pod_name, exec_command]

def kubectl_mode(stdscr):
    from kubectl.pod import Pods
    curses.cbreak()
    stdscr.keypad(True)
    Color.init()
    try:
        namespace = Config()["default"]["kubectl"]["namespace"]
    except:
        namespace = None
    pods = Pods(get_kube_pods(namespace))
    while True:
        if len(pods.list) == 0:
            stdscr.addstr(0, 0, "empty runnning pods.", Color.get("RED_WHITE"))
        for i, l in enumerate(pods.list):
            stdscr.addstr(i, 0, "{}".format(l.metadata.name), Color.get("BLUE"))
        stdscr.move(pods.index, 0);
        c = stdscr.getch()
        if c in [curses.KEY_ENTER, KeyPad.ENTER]:
            curses.nocbreak() 
            stdscr.keypad(False)
            stdscr.clear()
            subprocess.call(["clear"])
            exec_command = "/bin/sh"
            subprocess.call(get_command(pods.current_pod.metadata.name, pods.current_pod.metadata.namespace, exec_command))
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
        elif c == ord('X'):
            win = curses.newwin(1, curses.COLS-1, curses.LINES-1, 0)
            box = Textbox(win)
            box.edit()
            command = box.gather().rstrip()

            curses.nocbreak() 
            stdscr.keypad(False)
            stdscr.clear()
            subprocess.call(["clear"])
            subprocess.call(get_command(pods.current_pod.metadata.name, pods.current_pod.metadata.namespace, command))
            curses.cbreak() 
            stdscr.keypad(True) 
        elif c == ord('q'):
            break
    curses.nocbreak()
    stdscr.keypad(False)
    curses.echo()
    curses.endwin()

def get_kube_pods(namespace=None):
    Client.load_config()
    client = Client()
    if namespace:
        return client.list_namespaced_pod(namespace, watch=False)
    else:
        return client.list_pod_for_all_namespaces(watch=False)
