# CATCH THE EGG


```python
from itertools import cycle
from random import randrange
from tkinter import Tk , Canvas , messagebox , font

canvas_width = 800
canvas_height = 400

win = Tk()
c = Canvas(win , width = canvas_width ,  height = canvas_height , background = 'deep sky blue')
c.create_rectangle(-5, canvas_height - 100 , canvas_width + 5 , canvas_height + 5 , fill='sea green', width=0)
c.create_oval(-80,-80,120,120,fill='orange' , width=0)
c.pack()

color_cycle = cycle(['light blue' , 'light pink' , 'light yellow','light green' , 'red', 'blue' , 'green','black'])
egg_width = 45
egg_height = 55
egg_score = 10
egg_speed = 90
egg_interval = 2000
difficulty_factor = 0.95

catcher_color = 'blue'
catcher_width = 100
catcher_height = 100
catcher_start_x = canvas_width / 2 - catcher_width / 2
catcher_start_y = canvas_height -catcher_height - 20
catcher_start_x2 = catcher_start_x + catcher_width
catcher_start_y2 = catcher_start_y + catcher_height

catcher = c.create_arc(catcher_start_x ,catcher_start_y ,catcher_start_x2,catcher_start_y2 , start=200 , extent = 140 , style='arc' , outline=catcher_color , width=3)

score = 0
score_text = c.create_text(10,10,anchor='nw' , font=('Arial',18,'bold'),fill='darkblue',text='Score : ' + str(score))

lives_remaning = 3
lives_text = c.create_text(canvas_width-10,10,anchor='ne' , font=('Arial',18,'bold'),fill='darkblue',text='Lives : ' + str(lives_remaning))

eggs = []

def create_eggs():
    x = randrange(10,740)
    y = 40
    new_egg = c.create_oval(x,y,x+egg_width,y+egg_height,fill=next(color_cycle),width=0)
    eggs.append(new_egg)
    win.after(egg_interval,create_eggs)

def move_eggs():
    for egg in eggs:
        (egg_x,egg_y,egg_x2,egg_y2) = c.coords(egg)
        c.move(egg,0,10)
        if egg_y2 > canvas_height:
            egg_dropped(egg)
    win.after(egg_speed,move_eggs)

def egg_dropped(egg):
    eggs.remove(egg)
    c.delete(egg)
    lose_a_life()
    if lives_remaning == 0:
        messagebox.showinfo('GAME OVER!' , 'Final Score : ' + str(score))
        win.destroy()

def lose_a_life():
    global lives_remaning
    lives_remaning -= 1
    c.itemconfigure(lives_text , text='Lives : ' + str(lives_remaning))

def catch_check():
    (catcher_x,catcher_y,catcher_x2,catcher_y2) = c.coords(catcher)
    for egg in eggs:
        (egg_x,egg_y,egg_x2,egg_y2) = c.coords(egg)
        if catcher_x < egg_x and egg_x2  < catcher_x2 and catcher_y2 - egg_y2 < 40:
            eggs.remove(egg)
            c.delete(egg)
            increase_score(egg_score)
    win.after(100,catch_check)

def increase_score(points):
    global score , egg_speed , egg_interval
    score += points
    egg_speed = int(egg_speed * difficulty_factor)
    egg_interval = int(egg_interval * difficulty_factor)
    c.itemconfigure(score_text , text='Score : ' + str(score))

def move_left(event):
    (x1,y1,x2,y2) = c.coords(catcher)
    if x1 > 0:
        c.move(catcher,-20,0)

def move_right(event):
    (x1,y1,x2,y2) = c.coords(catcher)
    if x2 < canvas_width:
        c.move(catcher,20,0)

c.bind('<Left>' , move_left)
c.bind('<Right>' , move_right)
c.focus_set()

win.after(1000,create_eggs)
win.after(1000,move_eggs)
win.after(1000,catch_check)

win.mainloop()
```

# COLOUR GUESS GAME


```python
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 10 22:27:40 2024

@author: varun g
"""

import random
import tkinter as tk
from tkinter import messagebox

colours = ['Red', 'Blue', 'Green', 'Yellow', 'Orange', 'Purple', 'Pink', 'Black', 'White']
score = 0
timeleft = 30

def next_colour():
    global score, timeleft

    if timeleft > 0:
        user_input = e.get().lower()
        correct_color = colours[1].lower()

        if user_input == correct_color:
            score += 1

        e.delete(0, tk.END)
        random.shuffle(colours)
        label.config(fg=colours[1], text=colours[0])
        score_label.config(text=f"Score: {score}")


def countdown():
    global timeleft
    if timeleft > 0:
        timeleft -= 1
        time_label.config(text=f"Time left: {timeleft}")
        time_label.after(1000, countdown)
    else:
    # messagebox.showwarning ('Attention', 'Your time is out!!')
        scoreshow()
        

def record_highest_score():
    highest_score = load_highest_score()
    if score > highest_score:
        with open("highest_score.txt", "w") as file:
            file.write(str(score))
    


def load_highest_score():
    try:
        with open("highest_score.txt", "r") as file:
            data = file.read()
            if data:
                return int(data)
            else:
                return 0
    except FileNotFoundError:
        return 0


def scoreshow():
    record_highest_score()
    window2 = tk.Tk()
    window2.title("HIGH SCORE")
    window2.geometry("300x200")

    label = tk.Label(window2, text=f"Highest Score: {load_highest_score()}",font=(font, 12))
   
    label.pack()

    window2.mainloop()

def start_game(event):
    global timeleft
    if timeleft == 30:
        countdown()
    next_colour()

window = tk.Tk()
font = 'Helvetica'
window.title("Color Game")
window.geometry("375x250")
window.resizable(False, False)

instructions = tk.Label(window, text="Enter the color of the text, not the word!", font=(font, 12))
instructions.pack(pady=10)

score_label = tk.Label(window, text="Press Enter to start", font=(font, 12))
score_label.pack()
 
time_label = tk.Label(window, text=f"Time left: {timeleft}", font=(font, 12))
time_label.pack()

label = tk.Label(window, font=(font, 60))
label.pack(pady=20)

e = tk.Entry(window)
window.bind('<Return>', start_game)
e.pack()

e.focus_set()

window.mainloop()
```

# FLAPPY BIRD 


```python
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 11 15:07:57 2024

@author: varung
"""
import pygame
import sys
import random

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 600, 400
FPS = 60
GRAVITY = 0.5
BIRD_JUMP = 10
PIPE_SPEED = 5

# Colors
WHITE = (255, 255, 255)

# Create the window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Flappy Bird")

# Load images
bird_image = pygame.image.load("bird1.png")  # Replace with your bird image
pipe_image = pygame.image.load("pipe.png")  # Replace with your pipe image

# Bird class
class Bird:
    def __init__(self):
        self.x = 100
        self.y = HEIGHT // 2
        self.velocity = 0

    def jump(self):
        self.velocity = -BIRD_JUMP

    def update(self):
        self.velocity += GRAVITY
        self.y += self.velocity

    def draw(self):
        screen.blit(bird_image, (self.x, int(self.y)))

# Pipe class
class Pipe:
    def __init__(self):
        self.x = WIDTH
        self.gap = 150
        self.height = random.randint(50, HEIGHT - 50 - self.gap)

    def move(self):
        self.x -= PIPE_SPEED

    def off_screen(self):
        return self.x + pipe_image.get_width() < 0

    def draw(self):
        screen.blit(pipe_image, (self.x, 0))
        screen.blit(pipe_image, (self.x, self.height + self.gap))

# Main game loop
clock = pygame.time.Clock()
bird = Bird()
pipes = []
exit_game = False  # Flag to indicate whether to exit the game

while not exit_game:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit_game = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                bird.jump()

    # Update
    bird.update()
    for pipe in pipes:
        pipe.move()

    # Generate new pipes
    if random.randint(1, 100) < 10:
        pipes.append(Pipe())

    # Remove off-screen pipes
    pipes = [pipe for pipe in pipes if not pipe.off_screen()]

    # Check for collisions
    for pipe in pipes:
        if (
            bird.x < pipe.x + pipe_image.get_width()
            and bird.x + bird_image.get_width() > pipe.x
            and (bird.y < pipe.height or bird.y + bird_image.get_height() > pipe.height + pipe.gap)
        ):
            print("Collision detected!")
            exit_game = True
            break  # Exit the loop on collision

    # Draw
    screen.fill(WHITE)
    bird.draw()
    for pipe in pipes:
        pipe.draw()

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
sys.exit()

```

# HANG MAN GAME 


```python
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 11 14:53:15 2024

@author: varung
"""

import random

def choose_word():
    return random.choice(["tiger", "superman", "thor", "doraemon", "avenger", "water", "stream", "boy", "girl"])

def display_word(word, guessed_letters):
    return ' '.join(letter if letter in guessed_letters else '_' for letter in word)

def hangman():
    word = choose_word()
    valid_letters = 'abcdefghijklmnopqrstuvwxyz'
    turns = 10
    guessed_letters = set()

    print("Welcome to Hangman!")
    name = input("Enter your name: ")
    print(f"Welcome, {name}!")
    print("=====================")

    while turns > 0:
        guess = input(f"Guess the word: {display_word(word, guessed_letters)}\n").casefold()

        if guess in valid_letters:
            guessed_letters.add(guess)
        else:
            print("Enter a valid character")
            continue

        if guess not in word:
            turns -= 1

        print(f"{turns} turns left")
        draw_hangman(turns)

        if set(word) <= guessed_letters:
            print(f"Congratulations, {name}! You win!")
            break

    else:
        print("You lose")
        print(f"Sorry, {name}. The word was '{word}'.")

def draw_hangman(turns):
    hangman_parts = [
        ["  ---------  "],
        ["      O      "],
        ["   \  |  /   "],
        ["    \ | /    "],
        ["      |      "],
        ["     / \     "],
        ["-------------"]
    ]

    for part in hangman_parts[:10 - turns]:
        print(part[0])

hangman()
```

# PING PONG GAME


```python
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 11 15:19:18 2024

@author: varun g
"""

import pygame
import sys
import random

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 600, 400
PADDLE_WIDTH, PADDLE_HEIGHT = 15, 60
BALL_SIZE = 15
FPS = 60
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Create the game window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Simple Pong Game")

# Initialize paddles and ball
player_paddle = pygame.Rect(30, HEIGHT // 2 - PADDLE_HEIGHT // 2, PADDLE_WIDTH, PADDLE_HEIGHT)
opponent_paddle = pygame.Rect(WIDTH - 30 - PADDLE_WIDTH, HEIGHT // 2 - PADDLE_HEIGHT // 2, PADDLE_WIDTH, PADDLE_HEIGHT)
ball = pygame.Rect(WIDTH // 2 - BALL_SIZE // 2, HEIGHT // 2 - BALL_SIZE // 2, BALL_SIZE, BALL_SIZE)

# Set initial ball speed
ball_speed_x = 5 * random.choice([1, -1])
ball_speed_y = 5 * random.choice([1, -1])

# Set initial paddle speed
paddle_speed = 7

# Game loop
clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Move paddles
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP] and player_paddle.top > 0:
        player_paddle.y -= paddle_speed
    if keys[pygame.K_DOWN] and player_paddle.bottom < HEIGHT:
        player_paddle.y += paddle_speed

    # Move opponent paddle (simple AI)
    if opponent_paddle.centery < ball.centery and opponent_paddle.bottom < HEIGHT:
        opponent_paddle.y += paddle_speed
    elif opponent_paddle.centery > ball.centery and opponent_paddle.top > 0:
        opponent_paddle.y -= paddle_speed

    # Move the ball
    ball.x += ball_speed_x
    ball.y += ball_speed_y

    # Ball collisions with walls
    if ball.top <= 0 or ball.bottom >= HEIGHT:
        ball_speed_y = -ball_speed_y

    # Ball collisions with paddles
    if ball.colliderect(player_paddle) or ball.colliderect(opponent_paddle):
        ball_speed_x = -ball_speed_x

    # Scoring
    if ball.left <= 0 or ball.right >= WIDTH:
        # Reset ball position
        ball.x = WIDTH // 2 - BALL_SIZE // 2
        ball.y = HEIGHT // 2 - BALL_SIZE // 2
        # Randomize ball direction
        ball_speed_x = 5 * random.choice([1, -1])
        ball_speed_y = 5 * random.choice([1, -1])

    # Draw everything
    screen.fill(BLACK)
    pygame.draw.rect(screen, WHITE, player_paddle)
    pygame.draw.rect(screen, WHITE, opponent_paddle)
    pygame.draw.ellipse(screen, WHITE, ball)

    # Draw the center line
    pygame.draw.aaline(screen, WHITE, (WIDTH // 2, 0), (WIDTH // 2, HEIGHT))

    # Update the display
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(FPS)
```

# SNAKE GAME 


```python
import turtle as t
import random as rd

t.bgcolor('yellow')

caterpillar = t.Turtle()
caterpillar.shape('square')
caterpillar.speed(0)
caterpillar.penup()
caterpillar.hideturtle()

leaf = t.Turtle()
leaf_shape = ((0,0),(14,2),(18,6),(20,20),(6,18),(2,14))
t.register_shape('leaf', leaf_shape)
leaf.shape('leaf')
leaf.color('green')
leaf.penup()
leaf.hideturtle()
leaf.speed()

game_started = False
text_turtle = False
text_turtle = t.Turtle()
text_turtle.write('Press SPACE to start', align='center', font=('Arial', 18, 'bold'))
text_turtle.hideturtle()

score_turtle = t.Turtle()
score_turtle.hideturtle()
score_turtle.speed(0)

def outside_window():
    left_wall = -t.window_width()/2
    right_Wall = t.window_width()/2
    top_wall = t.window_height()/2
    bottom_wall = -t.window_height()/2
    (x,y) = caterpillar.pos()
    outside = x < left_wall or x > right_Wall or y > top_wall or y < bottom_wall
    return outside

def game_over():
    caterpillar.color('yellow')
    leaf.color('yellow')
    t.penup()
    t.hideturtle()
    t.write('GAME OVER !', align='center', font=('Arial', 30, 'normal') )
    t.onkey(start_game,'space')

def display_score(current_score):
    score_turtle.clear()
    score_turtle.penup()
    x = (t.window_width()/2) - 70
    y = (t.window_height()/2) - 70
    score_turtle.setpos(x,y)
    score_turtle.write(str(current_score), align='right', font=('Arial', 40, 'bold'))

def place_leaf():
    leaf.hideturtle()
    leaf.setx(rd.randint(-200,200))
    leaf.sety(rd.randint(-200,200))
    leaf.showturtle()

def start_game():
    global game_started
    if game_started:
        return
    game_started = True
    
    score = 0
    text_turtle.clear()

    caterpillar_speed = 2
    caterpillar_length = 3
    caterpillar.shapesize(1,caterpillar_length,1)
    caterpillar.showturtle()
    display_score(score)
    place_leaf()

    while True:
        caterpillar.forward(caterpillar_speed)
        if caterpillar.distance(leaf) < 20:
            place_leaf()
            caterpillar_length = caterpillar_length + 1
            caterpillar.shapesize(1,caterpillar_length,1)
            caterpillar_speed = caterpillar_speed + 1
            score = score + 10
            display_score(score)
        if outside_window():
            game_over()
            break

def move_up():
        caterpillar.setheading(90)

def move_down():
        caterpillar.setheading(270)

def move_left():
        caterpillar.setheading(180)

def move_right():
        caterpillar.setheading(0)
        
def restart_game():
 start_game()

t.onkey(start_game,'space')
t.onkey(restart_game,'Up')
t.onkey(move_up,'Up')
t.onkey(move_right,'Right')
t.onkey(move_down,'Down')
t.onkey(move_left,'Left')
t.listen()
t.mainloop()
```

# TICK-TAE-TOE  GAME


```python
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 11 15:12:21 2024

@author: varung
"""

import os

#initialize 
board = [' ' for x in range(10)]
FirstRun = True

#insert tic tac toe symbol to screen
def insertLetter(letter,pos):
    if(board.count(' ') >= 1):
        board[pos] = letter

def spaceIsFree(pos):
    return board[pos] == ' '

def printBoard(board):
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('-----------')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('-----------')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])

def isBoardFull(board):
    if board.count(' ') >= 2:
        return False
    else:
        return True


def IsWinner(b,l):
    return(
    (b[1] == l and b[2] == l and b[3] == l) or
    (b[4] == l and b[5] == l and b[6] == l) or
    (b[7] == l and b[8] == l and b[9] == l) or
    (b[1] == l and b[4] == l and b[7] == l) or
    (b[2] == l and b[5] == l and b[8] == l) or
    (b[3] == l and b[6] == l and b[9] == l) or
    (b[1] == l and b[5] == l and b[9] == l) or
    (b[3] == l and b[5] == l and b[7] == l)
    )

def playerMove():
    run = True
    while run:
        move = input("please select a position to enter the X between 1 to 9: ")
        try:
            move = int(move)
            if move > 0 and move < 10:
                if spaceIsFree(move):
                    run = False
                    insertLetter('X', move)
                else:
                    print('Sorry, this space is occupied')
            else:
                print('please type a number between 1 and 9')
        
        except:
            print('Please type a number')

def computerMove():
    possibleMoves = [ x for x, letter in enumerate(board) if letter == ' ' and x != 0]
    move = 0

    for let in ['O', 'X']:
        for i in possibleMoves:
            boardcopy = board[:]
            boardcopy[i] = let
            if IsWinner(boardcopy, let):
                move = i
                return move

    cornersOpen = []
    for i in possibleMoves:
        if i in [1, 3, 7, 9]:
            cornersOpen.append(i)

    if len(cornersOpen) > 0:
        move = selectRandom(cornersOpen)
        return move

    if 5 in possibleMoves:
        move = 5
        return move

    edgesOpen = []
    for i in possibleMoves:
        if i in [2, 4, 6, 8]:
            edgesOpen.append(i)

    if len(edgesOpen) > 0:
        move = selectRandom(edgesOpen)
        return move

def selectRandom(li):
    import random
    ln = len(li)
    r = random.randrange(0, ln)
    return li[r]

def StartTheGame():
    global board
    board = [' ' for x in range(10)]
    CleanScreen()
    print('-------------------------')
    GamePlay()

#clean Old data in screen when event occur
def CleanScreen():
    #Linux and macOS
    if(os.name == 'posix'):
         os.system('clear') 
    #windows
    else:
         os.system('cls')



#check Tie Game condition
def TieGame():
    
    if isBoardFull(board) and (not((IsWinner(board, 'X')) or (IsWinner(board, 'O')))):
        return True
    else:
        return False

#Score Count
scorecount = 0
#gameplay design here
def GamePlay():
    global scorecount
    if scorecount == 0:
        #if the game is first time ran
        print("Welcome to the game!")
    if scorecount < 0:
        #if the score is negative, set it to 0
        scorecount = 0
    printBoard(board)

    while not(isBoardFull(board)):
        
        if not(IsWinner(board, 'O')) :
            playerMove()
            CleanScreen()
            printBoard(board)
        else:
            scorecount -= 1
            print(f"Sorry, you lose 😢! Your Score is {scorecount}")
            break

        if (not(IsWinner(board, 'X'))) :
            move = computerMove()
            if move == 0:
                print(" ")
            elif not(isBoardFull(board)):
                insertLetter('O', move)
                print('computer placed an o on position', move, ':')
                CleanScreen()
                printBoard(board)
        else:
            scorecount += 1
            print(f"You win! Your Score is {scorecount}")
            break     
        

while True:
    if FirstRun:
        FirstRun=False
        StartTheGame()

    else :
        if TieGame():
            print("It's a tie!")
        x = input("Do you want to play again? (y/n)")
        if x.lower() == 'y' or x.lower() =='yes':
            StartTheGame()
        
        else:
            print("END Thank you")
            break
```


```python

```
