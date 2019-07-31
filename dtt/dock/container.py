class Containers:
    def __init__(self, containers):
        self._index = 0
        self._containers = containers
    @property
    def index(self):
        return self._index
    @property
    def current_container(self):
        return self._containers[self._index]
    @property
    def list(self):
        return self._containers
    def set_index(self, index):
        self._index = index
    def add_index(self):
        if self._index + 1 < len(self._containers):
            self._index += 1
    def sub_index(self):
        if 0 <= self._index - 1:
            self._index -= 1
