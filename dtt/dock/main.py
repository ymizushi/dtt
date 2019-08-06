import subprocess
import curses
from colors import Color
from curses import wrapper
import docker
from dock.container import Containers
from help import help_mode
from curses.textpad import Textbox 
from keypad import KeyPad
from mode import mode_gen

def get_command(container_id, exec_command, namespace=None):
    return ["docker", "exec", "-i", "-t", container_id, exec_command]

def gen_docker_mode():
    client = docker.from_env()
    containers = Containers(client.containers.list())
    return mode_gen('container', containers, get_command)
