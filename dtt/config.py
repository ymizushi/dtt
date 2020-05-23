from os.path import expanduser
import toml

class Config:
    def __init__(self):
        self._path = '{}/.config/dtt/config.toml'.format(expanduser("~"))
        self._toml_string = ""
        try:
            with open(self._path) as f:
                self._toml_string = f.read()
        except FileNotFoundError:
            self._toml_string = ""

    def __getitem__(self, item):
        return self.to_dic[item]
    @property
    def to_dic(self):
        return toml.loads(self._toml_string)
    @property
    def to_s(self):
        return self._toml_string
