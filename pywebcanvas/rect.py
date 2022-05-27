from __future__ import annotations

import js
from colour import Color
import pywebcanvas as pwc


class Rect:
    """
    A class used to create and interact with a rect shape.
    """
    def __init__(self, x: int, y: int, width: int, height: int, 
                 color: str="black", type_: str="fill") -> None:
        """
        Parameters
        ----------
        x: int
           x position on the canvas
        y: int
           y position on the canvas
        width: int
               Width of rect shape
        height: int
               height of rect shape
        color: str, optional
               Color of rect shape. Defaults is black
        type_: str, optional
               Type of rect (fill, stroke, clear). Default is fill
        """
        self.x, self.y = x, y
        self.width = width
        self.height = height
        self.color = color
        self.type_ = type_
    
    def render(self, canvas: pwc.Canvas):
        """
        Renders the rect shape on the canvas

        Parameters
        ----------
        canvas: pywebcanvas.Canvas
                An instance of pywebcanvas.Canvas
        """
        pwc.log(f"Render Rect {self} at x {self.x}, y {self.y}, width {self.width}, height {self.height}, color {self.color}, type_ {self.type_}")

        ctx = canvas.ctx()

        hex_color = Color(self.color).hex 
        ctx.fillStyle = hex_color

        args = (self.x, self.y, self.width, self.height)

        if self.type_ == "fill":
            ctx.fillRect(*args)
        elif self.type_ == "stroke":
            ctx.strokeRect(*args)
        elif self.type_ == "clear":
            ctx.clearRect(*args)
