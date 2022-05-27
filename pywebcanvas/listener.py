import js
import pyodide
from typing import Callable
import pywebcanvas as pwc


def add_event_handler(event: str, handler: Callable) -> None:
    """
    Add event handler between javascript events and python callables.

    Parameters
    ---------
    event: str
           Javascript event that serves as the trigger. See 
           https://developer.mozilla.org/en-US/docs/Web/Events .
    handler: Callable
           Python Callable to be called following the trigger. Should have a 
           single parameter.
    """
    pwc.log(f"Add event handler {handler} for event {event}")
    proxy = pyodide.create_proxy(handler)
    js.document.addEventListener(event, proxy)
