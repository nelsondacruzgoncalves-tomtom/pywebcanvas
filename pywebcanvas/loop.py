from typing import Awaitable, List
import asyncio
import pywebcanvas as pwc

class Loop:
    """
    A class to simplify interaction with the event loop.

    Attributes
    ----------
    loop: pyodide.webloop.Webloop
          Handle for the event loop 
    tasks: List[Awaitable]
           A list of the tasks that run on each iteration of the event loop.
    """
    def __init__(self) -> None:
        self.loop = asyncio.get_event_loop()
        self.tasks = []

    def add_task(self, task_name: str, task_func: Awaitable) -> None:
        """
        Add a task to the event loop.

        Parameters
        ----------
        task_name: str
                   Name of the task. Will be used during logging.
        task_func: Awaitable
                   The Python Awaitable to call.
        """
        pwc.log(f"Create task {task_name} {task_func}")
        self.tasks.append(task_func)
    
    def run(self) -> None:
        """
        Runs the event loop. Errors will be logged if logging is enabled.
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
