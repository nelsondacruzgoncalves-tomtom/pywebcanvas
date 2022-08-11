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
    
    def bezier_curve_to(self, c1_x_pos, c1_y_pos, c2_x_pos, c2_y_pos, x_pos, y_pos):
        pwc.log(f"Path {self} bezier curve to {x_pos}, {y_pos} with control points ({c1_x_pos}, {c1_y_pos}), ({c2_x_pos}, {c2_y_pos})")
        self.queue.append(("bezier_curve_to", (c1_x_pos, c1_y_pos, c2_x_pos, c2_y_pos, x_pos, y_pos)))

    def quadratic_curve_to(self, c_x_pos, c_y_pos, x_pos, y_pos):
        pwc.log(f"Path {self} quadratic curve to {x_pos}, {y_pos} with control point ({c_x_pos}, {c_y_pos})")
        self.queue.append(("quadratic_curve_to", (c_x_pos, c_y_pos, x_pos, y_pos)))

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
            elif action[0] == "bezier_curve_to":
                ctx.bezierCurveTo(*action[1])
            elif action[0] == "quadratic_curve_to":
                ctx.quadraticCurveTo(*action[1])
            elif action[0] == "fill":
                if not action[1] == "":
                    hex_color = Color(action[1]).hex 
                    ctx.fillStyle = hex_color
                ctx.fill()