import swengine
import swauto


##############################################Swift Basic Functions###########################################
def swift_wake():
    a = swengine.input()
    #a="search for cars24.com"
    c = 0
    list = ["stop", "play", "volume", "open", "quit", "turn", "weather", "shutdown"]
    for i in range(0, 8):
        if list[i] in a:
            K = list[i]
            c = c + 1
    if c > 0:
        repl_char = ""
        temp = a.split(" ")
        for idx in range(len(temp)):
            ele = temp[idx]
            if not ele == K:
                temp[idx] = repl_char
        res = "".join(temp)
    else:
        res = "web"

    thisdict = {
        "play": swengine.play,
        "stop": swengine.stopmusic,
        "volume": swengine.setvol,
        "open": swengine.openinswift,
        "quit": swengine.quitinswift,
        "turn": swauto.new,
        "weather": swengine.wehth,
        "shutdown": swengine.shutdown,
        "web": swengine.search_web
    }

    thisdict[res](a)


##############################################Swift Basic Skills###########################################

