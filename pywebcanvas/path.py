from __future__ import annotations

import js
from colour import Color
import pywebcanvas as pwc

class Path:
    def __init__(self, color="black"):
        self.color = color
        self.queue = []

    def begin_path(self):
        pwc.log(f"Begin Path {self}")
        self.queue.append(("begin_path", ()))

    def move_to(self, x_pos, y_pos):
        pwc.log(f"Path {self} move to {x_pos}, {y_pos}")
        self.queue.append(("move_to", (x_pos, y_pos)))

    def line_to(self, x_pos, y_pos, color=""):
        pwc.log(f"Path {self} line to {x_pos}, {y_pos}")
        self.queue.append(("line_to", (x_pos, y_pos)))

    def fill(self, color=""):
        pwc.log(f"Fill Path {self}")
        self.queue.append(("fill", (color)))

    def render(self, canvas):
        pwc.log(f"Render Path {self} with queue: {self.queue}")

        ctx = canvas.ctx()
        hex_color = Color(self.color).hex 
        ctx.fillStyle = hex_color

        for action in self.queue:
            if action[0] == "begin_path":
                ctx.beginPath()
            elif action[0] == "move_to":
                ctx.moveTo(*action[1])
            elif action[0] == "line_to":
                ctx.lineTo(*action[1])
            elif action[0] == "fill":
                if not action[1] == "":
                    hex_color = Color(action[1]).hex 
                    ctx.fillStyle = hex_color
                ctx.fill()