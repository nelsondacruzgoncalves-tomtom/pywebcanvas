import pywebcanvas as pwc                                                                                                            
    
canvas = pwc.Canvas(400, 400)                                                                                                        
canvas.background.fill("black")

path = pwc.Path(color="yellow")

path.begin_path()
path.move_to(200, 300)
path.line_to(150, 200)
path.line_to(100, 300)
path.fill()

path.begin_path()
path.move_to(250, 200)
path.line_to(200, 100)
path.line_to(150, 200)
path.fill()

path.begin_path()
path.move_to(200, 300)
path.line_to(250, 200)
path.line_to(300, 300)
path.fill()

canvas.render(path)
