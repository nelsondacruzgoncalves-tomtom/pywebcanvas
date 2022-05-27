from __future__ import annotations

import js
import pywebcanvas as pwc
from typing import TYPE_CHECKING, Union
if TYPE_CHECKING:
    import pyodide


class Canvas:
    """
    Class used to interact with the html canvas.

    Attributes
    ----------
    width: int
           Width of canvas
    height: int
           Height of canvas
    background: pywebcanvas.Background
           Instance of pywebcanvas.Background
    loop: pywebcanvas.Loop
           Instance of pywebcanvas.Loop
    """
    def __init__(self, width: int, height: int, parent: str="") -> None:
        """
        Parameters
        ----------
        width: int
               Width of canvas
        height: int
                Height of canvas
        parent: str, optional
                The canvas will be created as a child of the html element with 
                this id. If not specified, the canvas will be created as a 
                child of the body.
        """
        self.width, self.height = width, height
        self.canvas = js.document.createElement('canvas')
        self.canvas.setAttribute('width', self.width)
        self.canvas.setAttribute('height', self.height)
        self.background = pwc.Background(self)
        self.loop = pwc.Loop()

        if parent == "":
            js.document.body.appendChild(self.canvas)
            if pwc.logging:
                pwc.log(f"Create {self} with {width=}, {height=}")
        else:
            js.document.getElementById(parent).appendChild(self.canvas)
            pwc.log(f"Create {self} with {width=}, {height=}, {parent=}")
    
    def ctx(self) -> pyodide.JsProxy:
        """
        Returns canvas drawing context.
        """
        return self.canvas.getContext("2d")
    
    def render(self, item: Union[pwc.Rect, pwc.Text]) -> None:
        """
        "Renders" a canvas item (rect, text, etc.) by calling the item.render
        method with this canvas object as an argument.

        Parameters
        ---------
        item: Union[pywebcanvas.Rect, pywebcanvas.Text]
        """
        item.render(self)
    
    def clear(self) -> None:
        """
        Clears canvas.
        """
        pwc.log(f"Clear canvas")
        self.ctx().clearRect(0, 0, self.width, self.height)
