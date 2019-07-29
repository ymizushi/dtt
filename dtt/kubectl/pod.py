class Pods:
    def __init__(self, pods):
        self._index = 0
        self._pods = pods.items
        self._metadata = pods.metadata
    @property
    def index(self):
        return self._index
    @property
    def current_pod(self):
        return self._pods[self._index]
    @property
    def list(self):
        return self._pods

    def set_index(self, index):
        self._index = index
    def add_index(self):
        if self._index + 1 < len(self._pods):
            self._index += 1
    def sub_index(self):
        if 0 <= self._index - 1:
            self._index -= 1
