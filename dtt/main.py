#!/usr/bin/env python
# -*- coding: utf-8 -*-

from curses import wrapper
from docopt import docopt
from dock.main import docker_mode
from kubectl.main import kubectl_mode
from config import Config

__doc__ = """{f}
Usage: 
    {f} 
    {f} -k | --kubectl
    {f} -h | --help
    {f} -c | --config
Options:
    -k --kubectl             kubectl mode
    -h --help                Show this screen and exit.
    -c --config              Show config
""".format(f='dtt')


def main():
    args = docopt(__doc__)
    if args['--help']:
        pass
    elif args['--config']:
        print(Config().to_s)
    elif args['--kubectl']:
        wrapper(kubectl_mode)
    else:
        wrapper(docker_mode)

if __name__ == '__main__':
    main()
