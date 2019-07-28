from colors import Color

HELP_SENTENCES = """Quick reference for dtt keybindings:

[-] generic bindings
View switching
                           h view-help           Show help
View manipulation
                     <Enter> enter               Enter and exec /bin/sh selected line of container
                           q quit                quit dtt, or close current view if you open view
                           j up-current-line     up current line
                           k down-current-line   down current line"""

def help_mode(scr):
    scr.addstr(0, 0, HELP_SENTENCES, Color.get('YELLOW'))
    while True:
        if scr.getch() == ord('q'):
            scr.clear()
            break

