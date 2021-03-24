import swengine
import webbrowser


def fanon(self):
    webbrowser.open("http://192.168.0.113/26/off")


def fanoff(self):
    webbrowser.open("http://192.168.0.113/26/on")


def lighton(self):
    webbrowser.open("http://192.168.0.113/27/off")


def lightoff(self):
    webbrowser.open("http://192.168.0.113/27/on")


def new(command):
    command = command.replace("turn ", "")
    thisdict = {
        "on fan": fanon,
        "off fan": fanoff,
        "on light": lighton,
        "off light": lightoff
    }
    if thisdict[command](command) == 1:
        print("Using Automation")
