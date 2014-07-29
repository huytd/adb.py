from adb import ADB
debug = ADB()

print debug.devices()

debug.call("shell input keyevent 26")