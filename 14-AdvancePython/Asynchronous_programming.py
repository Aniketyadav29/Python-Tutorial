// Asynchronous Programming//
import time

def task(name):
    print(f"Start {name}")
    time.sleep(2)   # blocks execution
    print(f"End {name}")

task("A")
task("B")