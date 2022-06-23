from js import document
import pywebcanvas as pwc

class Image:
    def __init__(self, imagepath: str, x :int, y: int):
        self.id = str(self)
        self.img = document.createElement("img")
        self.img.src = imagepath
        self.x, self.y = x, y
        self.width, self.height = 0, 0

    def resize(self, NewWidth: int, NewHeight: int):
        self.width, self.height = NewWidth, NewHeight
        
    def check_size(self):
        if self.width + self.height == 0:
            self.width, self.height = self.img.width, self.img.height

    def render(self, canvas: pwc.Canvas):
        self.check_size()
        pwc.log(f"Render Image {self} at x {self.x}, y {self.y}, width {self.width}, height {self.height}, image {self.img.src}")
        ctx = canvas.ctx()
        args = (self.img, self.x, self.y, self.width, self.height)
        ctx = canvas.canvas.getContext("2d")
        ctx.drawImage(*args)
