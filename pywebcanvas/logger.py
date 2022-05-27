import js


logging: bool = True
"""
Whether pywebcanvas will log
"""

def log(message: str):
    """
    Logs message to console

    Parameters
    ----------
    message: str
             The message to log
    """
    global logging
    if logging:
        js.console.log(f"pywebcanvas: {message}")

def disable_logging(disable: bool):
    """
    Disables logging

    Parameters
    ----------
    disable: bool
             If True, logging will be disabled. If False, logging will be enabled.
    """
    global logging 
    logging = not disable
    log(f"{logging=}")
