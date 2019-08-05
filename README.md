dtt [![CircleCI](https://circleci.com/gh/ymizushi/dtt.svg?style=svg)](https://circleci.com/gh/ymizushi/dtt)
============

dtt is the text-mode interface for docker and kubectl command.
the ui of dtt is inspired by vim, ranger and tig.

# Install

```sh
pip install dtt
```

# Usage

```sh
Usage: 
    dtt 
    dtt -k | --kubectl
    dtt -h | --help
    dtt -c | --config
Options:
    -k --kubectl             kubectl mode
    -h --help                Show this screen and exit.
    -c --config              Show config
```

A main usecase for dtt is to login container or pod with shell.

Exec `dtt` command and move to container with j or k key (like vim) and press Enter-key when you want to login the container or pod.

![screenshot](https://user-images.githubusercontent.com/788785/61949937-57642d80-afe7-11e9-9240-6f3798432a25.gif)

You can exec another shell or command with `X` key when you select the container or pod.

# Customize setting

Install below file on `$HOME/.config/dtt/config.toml`

```toml
[default]
  shell = "/bin/sh"
  logging_dir = "/tmp/dtt.log"
[default.kubectl]
  namespace = "sample-namespace"
```

you can set default shell, looging directory, and default k8s namespace.

# Development

see [README_DEV.md](https://github.com/ymizushi/dtt/blob/master/README_DEV.md)
