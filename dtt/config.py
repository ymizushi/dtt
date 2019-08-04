from os.path import expanduser
import toml

DEFAULT_SHELL='/bin/sh'

class Config:
    def __init__(self, path=None):
        if path:
            self._path = path
        else:
            self._path = '{}/.config/dtt/config.toml'.format(expanduser("~"))
        with open(self._path) as f:
            self._toml_string = f.read()
    def __getitem__(self, item):
        return self.to_dic[item]
    @property
    def to_dic(self):
        return toml.loads(self._toml_string)
    @property
    def to_s(self):
        return self._toml_string
