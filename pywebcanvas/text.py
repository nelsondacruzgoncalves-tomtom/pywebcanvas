import js
from colour import Color
import pywebcanvas as pwc


class Text:
    """
    A class used to create and interact with Text.
    """
    def __init__(self, text: str, x: int, y: int, size: int=20, 
                 color: str="black", font: str="helvetica", 
                 stroke: bool=False) -> None:
        """
        Parameters
        ----------
        text: str
              The content of the text to be displayed
        x: int
           x position on the canvas
        y: int
           y position on the canvas
        size: int, optional
              The font size of the text. Default is 20
        font: str, optional
              The font of the text. Default is helvetica
        stroke: bool, optional
                Whether the text is fill or stroke. Default is False (fill)
        """
        self.text = text
        self.x, self.y = x, y
        self.size = size
        self.color = color
        self.font = font
        self.stroke = stroke
    
    def render(self, canvas: pwc.Canvas) -> None:
        """
        Render the text on the canvas.

        Parameters
        ----------
        canvas: pywebcanvas.Canvas
                An instance of pywebcanvas.Canvas
        """
        pwc.log(f"Render text {self} at x {self.x}, y {self.y}, size {self.size}, color {self.color}, font {self.font}, stroke {self.stroke}")

        ctx = canvas.ctx()

        hex_color = Color(self.color).hex 

        ctx.fillStyle = hex_color
        ctx.font = f"{self.size}px {self.font}"

        if self.stroke:
            ctx.strokeText(self.text, self.x, self.y)
        else:
            ctx.fillText(self.text, self.x, self.y)
