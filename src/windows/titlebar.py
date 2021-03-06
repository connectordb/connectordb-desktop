# This script gathers the active titlebar text on "run"
import win32gui

# Workaround to get unicode working in both python 2 and 3
try:
    unicode = unicode
except:
    def unicode(txt, errors="lol"):
        # This is needed, because binary strings fail checks
        # of string schema
        if hasattr(txt, "decode"):
            txt = txt.decode()
        return txt


class StreamGatherer():
    streamname = "activewindow"
    streamschema = {"type": "string"}
    nickname = "Active Window"
    datatype = "window.titlebar"
    icon = "material:laptop_windows"
    description = "Gathers the currently active window's titlebar text"

    def __init__(self):
        self.prevtext = ""

    def start(self, cache):
        pass

    def stop(self):
        pass

    def run(self, cache):
        wt = self.windowtext()
        if wt != self.prevtext:
            self.prevtext = wt
            cache.insert(self.streamname, wt)

    # Gets the titlebar text of the currently active window
    def windowtext(self):
        return unicode(win32gui.GetWindowText(win32gui.GetForegroundWindow()), errors="ignore")
