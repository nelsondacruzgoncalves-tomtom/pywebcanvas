import js
import pywebcanvas as pwc


class Canvas:
    """
    Class used to interact with the canvas.
    """
    def __init__(self, width, height, parent=""):
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
    
    def ctx(self):
        """
        Returns canvas drawing context.
        """
        return self.canvas.getContext("2d")
    
    def render(self, item):
        item.render(self)
    
    def clear(self):
        """
        Clears canvas.
        """
        pwc.log(f"Clear canvas")
        self.ctx().clearRect(0, 0, self.width, self.height)
