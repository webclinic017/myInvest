from pywinauto.application import Application
import pywinauto

app = Application(backend="uia").start('Open API Login')


procs = pywinauto.findwindows.find_elements()

print(procs)
