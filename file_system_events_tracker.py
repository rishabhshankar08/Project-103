import sys
import time
import random
import os
import shutil
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

from_dir = "C:\Users\DELL\Desktop"

class FileEventHandler(FileSystemEventHandler):

    def on_created(self, event):
        print(f"Hey, {event.src_path} has been created!")
    def on_modified(self, event):
        print(f"Hey, someone made chnages to {event.src_path}!")
    def on_moved(self, event):
        print(f"Hey, someone moved {event.src_path} to a different directory!")
    def on_deleted(self, event):
        print(f"Hey someone deleted {event.src_path}!")

#Initialize Event Handler Class
event_handler = FileEventHandler()
#Initialize Observer
observer = Observer()
#Schedule the Observer
observer.schedule(event_handler, from_dir, True)
#Start the Observer
observer.start()

#Except Operator
try:
    while True:
        time.sleep(2)
        print("running")
except KeyboardInterrupt:
    print("stopped")
    observer.stop()