// Normal Method Programming//
import time

def task(name):
    print(f"Start {name}")
    time.sleep(2)   # blocks execution
    print(f"End {name}")

task("A")
task("B")

// Asynchronous programming //

import asyncio

async def task(name):
    print(f"Start {name}")
    await asyncio.sleep(2)   # non-blocking wait
    print(f"End {name}")

async def main():
    await asyncio.gather(
        task("A"),
        task("B")
    )

asyncio.run(main())
