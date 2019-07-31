#!/usr/bin/env python
# -*- coding: utf-8 -*-

from curses import wrapper
from docopt import docopt
from dock.main import docker_mode
from kubectl.main import kubectl_mode

__doc__ = """{f}
Usage: 
    {f} 
    {f} -k | --kubectl
    {f} -h | --help
Options:
    -k --kubectl             kubectl mode
    -h --help                Show this screen and exit.
""".format(f='dtt')


def main():
    args = docopt(__doc__)
    if args['--kubectl']:
        wrapper(kubectl_mode)
    elif args['--help']:
        pass
    else:
        # TODO: fix curses.error: addstr() returned ERR
        wrapper(docker_mode)

if __name__ == '__main__':
    main()
