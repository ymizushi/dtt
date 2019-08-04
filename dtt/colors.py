import curses

class Color:
    COLOR_MAP = {
        "YELLOW" : (1, curses.COLOR_YELLOW, curses.COLOR_BLACK),
        "CYAN" : (2, curses.COLOR_CYAN, curses.COLOR_BLACK),
        "BLUE" : (3, curses.COLOR_BLUE, curses.COLOR_BLACK),
        "RED_WHITE" : (4, curses.COLOR_RED, curses.COLOR_WHITE),
    }

    @classmethod
    def init(cls):
        # TODO: cache implementation
        for color in cls.COLOR_MAP.values():
            curses.init_pair(*color)

    @classmethod
    def get(cls, name):
        return curses.color_pair(cls.COLOR_MAP.get(name)[0])
