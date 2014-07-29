from adb import ADB
debug = ADB()

print debug.devices()

debug.shell("input keyevent 26")
debug.shell("input keyevent 82")
debug.shell("input swipe 50 50 800 50")

#debug.screenShot("./ss.png")