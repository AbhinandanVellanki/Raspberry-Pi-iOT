# Pong Client

import socket
from time import sleep
from sense_hat import SenseHat

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = ('192.168.1.1', 3542)
sock.connect(server_address)

sense = SenseHat()

y = 4
opponent = 4
ball_position = [3, 3]
ball_velocity = [1, 1]

def draw_bat():
    sense.set_pixel(7, y, 0, 255, 0)
    sense.set_pixel(7, y + 1, 0, 255, 0)
    sense.set_pixel(7, y - 1, 0, 255, 0)
    sense.set_pixel(0, opponent, 0, 0, 255)
    sense.set_pixel(0, opponent + 1, 0, 0, 255)
    sense.set_pixel(0, opponent - 1, 0, 0, 255)

def move_up(event):
    global y
    if y > 1 and event.action=='pressed':
        y -= 1

def move_down(event):
    global y
    if y < 6 and event.action=='pressed':
        y += 1

def draw_ball():
    global ball_position
    # Draws the ball pixel
    sense.set_pixel(ball_position[0], ball_position[1], 255, 255, 255)
    # # Moves the ball to the next position
    # ball_position[0] += ball_velocity[0]
    # ball_position[1] += ball_velocity[1]
    # # Ball hits player's bat
    # if ball_position[0] == 1 and y - 1 <= ball_position[1] <= y + 1:
    #     ball_velocity[0] = -ball_velocity[0]
    # # Ball hits opponent's bat
    # if ball_position[0] == 6 and opponent - 1 <= ball_position[1] <= opponent + 1:
    #     ball_velocity[0] = -ball_velocity[0]
    # # Ball hits side walls
    # if ball_position[1] == 0 or ball_position[1] == 7:
    #     ball_velocity[1] = -ball_velocity[1]
    # # Ball is not rebounced by either bat
    # if ball_position[0] == 0 or ball_position[0] == 7:
    #     ball_velocity[0] = -ball_velocity[0]

sense.stick.direction_up = move_up
sense.stick.direction_down = move_down

counter = 0

while True:
    sock.send(str(y).encode("utf-8"))
    incoming_y = sock.recv(1024)
    if incoming_y:
        data = incoming_y.decode("utf-8")
        array = data.split(',')
        if len(array) == 3:
            opponent = int(array[0])
            ball_position[0] = int(array[1])
            ball_position[1] = int(array[2])

    if counter >= 5:
        sense.clear(0, 0, 0)
        draw_bat()
        draw_ball()
        counter = 0
    else:
        counter += 1

    sleep(0.05)
