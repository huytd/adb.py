##adb.py
Write your Android custom debug script easily with Python

![Python ADB](http://i.imgur.com/1Ox9ilr.png?1)

###How to use
First, you need to import **adb.py** library
```python
from adb import ADB
```
Then, create your **debug** object
```python
debug = ADB()
```
After you created **debug** object, you can use it to execute adb commands.

###Examples
**List all connected devices**
```python
print debug.devices()
```
**Click POWER button to turn on screen**
```python
debug.call("shell input keyevent 26")
```
**Upload a file to Device**
```python
debug.upload("D:/data.zip","/sdcard/dataCopied.zip")
```
**Download a file from Device**
```python
debug.get("/sdcard/Download/arduino.pdf","D:/Books/Adruino.pdf")
```
**Install APK file to Device**
```python
debug.install("D:/Games/com.gamarist.murimuri-jump.apk")
```
or
```python
debug.install(("-r", "D:/Games/com.gamarist.number-tower.apk"))
```
**Uninstall an application on device**
```python
debug.uninstall("com.colrist.kimchi")
```
**Clear application data**
```python
debug.clearData("com.gamarist.murimuri")
```
**Run an application**
```python
debug.start("com.gamarist.murimuri/.MainActivity")
```
or
```python
debug.start(("com.gamarist.murimuri","MainActivity"))
```
**Kill an application**
```python
debug.kill("com.gamarist.murimuri")
```
**Execute shell command**
```python
debug.shell("input swipe 50 50 200 50")
```
**Change screen resolution**
This is useful to test your application in multiple screen size
```python
debug.screen("800x400")
```
To return to default resolution
```python
debug.screen("reset")
```
**Change screen DPI**
```python
debug.dpi("160")
```
**Record screen to video file**
```python
debug.screenRecord("/sdcard/record/output.mp4")
```
By default, the recording will stop after 3 minutes.
If you want to set the recording time, add a time parameter in seconds
```python
debug.screenRecord(("60", "/sdcard/record/output.mp4"))
```
**Take screenshot and save to local**
```python
debug.screenShot("D:/saved.png")
```