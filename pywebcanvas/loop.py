from typing import Awaitable
import asyncio
import pywebcanvas as pwc

class Loop:
    """
    A class to simplify interaction with the event loop.
    """
    def __init__(self):
        self.loop = asyncio.get_event_loop()
        self.tasks = []

    def add_task(self, task_name: str, task_func: Awaitable):
        """
        Add a task to the event loop. The task will be run on each iteration 
        of the event loop.
        """
        pwc.log(f"Create task {task_name} {task_func}")
        self.tasks.append(task_func)
    
    def run(self):
        """
        Run the event loop.
        """
        async def do_loop():
            pwc.log(f"Run loop {self} with tasks {self.tasks}")
            for func in self.tasks:
                try:
                    await func()
                except Exception as e:
                    pwc.log(f"task Error {e}")
            asyncio.ensure_future(do_loop())

        asyncio.ensure_future(do_loop())
        self.loop.run_forever()
