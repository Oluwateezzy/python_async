import threading
import threading

myData = threading.local()

myData.number = 12

print(myData.number)
print(myData.__dict__)
myData.__setattr__('widgets', [])

print(myData.widgets)

# Accessing data in different thread
log = []

def f():
    items = sorted(myData.__dict__.items())
    print(items)
    log.append(items)
    myData.number = 11
    log.append(myData.number)

thread = threading.Thread(target=f)
thread.start()
thread.join()

print(log)

class MyLocal(threading.local):
    number = 2
    def __init__(self, /, **kw):
        self.__dict__.update(kw)
    
    def squared(self):
        return self.number ** 2

myData = MyLocal(color="red")

print(myData.number)
print(myData.color)
del myData.color

print(myData.squared())

log = []
thread2 = threading.Thread(target=f)
print(thread2.is_alive())
thread2.start()
print(thread2.is_alive())
thread2.join(timeout=5)
print(thread2.is_alive())
print(log)