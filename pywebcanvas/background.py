from __future__ import annotations
import js
from colour import Color
import pywebcanvas as pwc


class Background:
    """
    A class used to interact with the background of the canvas.
    """
    def __init__(self, canvas: pwc.Canvas) -> None:
        """
        Parameters
        ----------
        canvas: pywebcanvas.Canvas
                An instance of pywebcanvas.Canvas
        """
        self.canvas = canvas

    def fill(self, color: str) -> None:
        """
        Set the background color of the canvas.
        Parameters
        ----------
        color : str
                The color used. Supported colors can be found at 
                https://www.w3.org/TR/css-color-3/#svg-color .
        """
        hex_color = Color(color).hex      
        pwc.log(f"Set {self.canvas} background to {hex_color}")
        self.canvas.canvas.setAttribute('style', f'background-color:{hex_color}')
