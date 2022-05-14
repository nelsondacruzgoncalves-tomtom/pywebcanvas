import js
from colour import Color
import pywebcanvas as pwc


class Background:
    """
    A class used to interact with the background of the canvas.
    """
    def __init__(self, canvas):
        self.canvas = canvas

    def fill(self, color):
        """
        Set the background color of the canvas.
        Parameters
        ----------
        color : str
                The color to change the background to. Can be in hexadecimal 
                format or most english color names.
        """
        hex_color = Color(color).hex      
        pwc.log(f"Set {self.canvas} background to {hex_color}")
        self.canvas.canvas.setAttribute('style', f'background-color:{hex_color}')
