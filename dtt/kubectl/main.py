import subprocess
import curses
from colors import Color
from help import help_mode

from kubectl.client import Client

def get_command(pod_name, namespace, exec_command):
    if namespace:
        return ["kubectl", "exec", "-i", "-t", "--namespace", namespace, pod_name, exec_command]
    else:
        return ["kubectl", "exec", "-i", "-t", pod_name, exec_command]

def kubectl_mode(stdscr):
    from kubectl.pod import Pods
    curses.cbreak()
    stdscr.keypad(True)
    Color.init()
    # TODO: implements namespace config
    namespace == None
    pods = Pods(get_kube_pods(namespace))
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
            # TODO: impl custome exec command
            exec_command = "/bin/bash"
            subprocess.call(get_command(pods.current_pod.metadata.name, namespace, exec_command))
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

def get_kube_pods(namespace=None):
    Client.load_config()
    client = Client()
    if namespace:
        return client.list_namespaced_pod(namespace, watch=False)
    else:
        return client.list_pod_for_all_namespaces(watch=False)
