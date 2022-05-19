import pywebcanvas as pwc
import random
import asyncio


canvas = pwc.Canvas(800, 600)
loop = pwc.Loop()
canvas.background.fill("black")
paddle_1 = pwc.Rect(100, 200, 15, 100, color="white")
paddle_2 = pwc.Rect(700, 200, 15, 100, color="white")
ball = pwc.Rect(400, 300, 30, 30, color="white")
ball_velocity = [1, 1]
score_data = [0, 0]
score = pwc.Text(f"{score_data[0]}:{score_data[1]}", 350, 50, size=30, color="white")
speed = 0.6

def player_movement(e):
    global paddle_2
    if e.code == "KeyW":
        paddle_2.y += -10
    elif e.code == "KeyS":
        paddle_2.y += 10

async def ai_movement():
    global paddle_1
    if paddle_1.y+(0.5*paddle_1.height) > ball.y+(0.5*ball.height):
        paddle_1.y += -1
    else:
        paddle_1.y += 1

def check_collision(x1, y1, w1, h1, x2, y2, w2, h2):
    if x1+w1 < x2 or x1 > x2+w2:
        return False
    if y1 > y2+h2 or y1+h1 < y2:
        return False
    return True

async def ball_movement():
    global ball
    global speed
    if ball.x+ball.width >= 800 or ball.x <= 0:
        ball_velocity[0] *= random.choice([-1, 1])
        ball_velocity[1] *= random.choice([-1, 1])
        ball.x, ball.y = 400, 300

    if ball.y+ball.height >= 600 or ball.y <= 0:
        ball_velocity[1] *= -1

    if check_collision(ball.x, ball.y, ball.width, ball.height, paddle_1.x, 
                       paddle_1.y, paddle_1.width, paddle_1.height) or (
       check_collision(ball.x, ball.y, ball.width, ball.height, paddle_2.x,
                       paddle_2.y, paddle_2.width, paddle_2.height)):
        ball_velocity[0] *= -1
        ball_velocity[1] *= random.choice([-1, 1])
        ball.x += ball_velocity[0] * speed * 15
        speed += 0.05

    ball.x += ball_velocity[0] * speed
    ball.y += -ball_velocity[1] * speed

async def check_score():
    global score_data
    global score
    global speed
    temp_score_data = score_data
    if ball.x+ball.width >= 800:
        score_data[0] += 1
        speed = 0.6
    elif ball.x <= 0:
        score_data[1] += 1
        speed = 0.6
    score.text = f"{score_data[0]}:{score_data[1]}"

async def on_update():
    await ball_movement()
    await ai_movement()
    await check_score()
    canvas.clear()
    canvas.render(paddle_1)
    canvas.render(paddle_2)
    canvas.render(ball)
    canvas.render(score)

pwc.add_event_handler("keydown", player_movement)
loop.add_task("on_update", on_update)
loop.run()
