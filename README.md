##adb.py
Write your Android custom debug script easily with Python

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

(...)
