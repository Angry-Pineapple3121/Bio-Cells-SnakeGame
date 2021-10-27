from tkinter import *
import random
import time

GAME_WIDTH = 1000
GAME_HEIGHT = 700
SPEED = 150
SPACE_SIZE = 50
BODY_PARTS = 3
SNAKE_COLOR = "#0000FF"
FOOD_COLOR = "#FF00FF"
BACKGROUND_COLOR = "#000000"
DEBUG = True
PRINT_NOTE_ON_GAME_END = True

NOTES_INDEX = [
    """
                            ☆ Nucleus ☆

    ★ Coordinates cell activities including growth, 
    intermediary metabolism, protein synthesis, 
    and reproduction. ★
    """,
    """
                ☆ Cytoplasm ☆

    ★ A jelly-like solution that
    fills the inside of the cell and
    surrounds other important parts
    of the cell. ★
    """,
    """
                        ☆ Mitochondrion ☆

    ★ Oblong-shaped organelles, found in the
    cytoplasm of cells In the animal cell, they are
    the main source of power for the cell. ★
    """,
    """
                        ☆ Rough ER ☆

    ★ Has ribosomes on it, which help to
    make proteins for the cell. The Rough ER 
    gets its name because of the ribosomes
    attached to it. ★
    """,
    """
                        ☆ Smooth ER ☆

    ★ The Smooth ER's job is to produce
    substances that are needed for the cell. ★
    """,
    """
                        ☆ Ribosome ☆

    ★ Tiny organelles are composed of 60%
    protein and 40% RNA. They help to
    make proteins and are attached 
    to the Rough ER. ★
    """,
    """
                        ☆ Golgi Body ☆

    ★ Also known as a Golgi Apparatus, this
    organelle helps to process and package
    proteins and lipid molecules. ★
    """,
    """
                    ☆ Cytoskeleton ☆

    ★ A structure that helps cells to keep
    their internal shape and provides
    mechanical support that assists
    in division and reproduction. ★
    """,
    """
                    ☆ Plasma Membrane ☆

    ★ Found in all cells. Separates the interior
    of the cell from the outside environment. ★
    """,
    """
                            ☆ Centrioles ☆

    ★ Self-replacing organelles are made up of
    nine bundles of microtubules. They assist in
    organizing cell divison. ★
    """,
    """
                        ☆ Lysosome ☆
                        
    ★ Think of a lysosome as a janitor.
    Lysosomes break down cellular waste and
    give the materials to the cytoplasm
    as new cell-building materials. ★
    """,
    """
                            ☆ DNA ☆

    ★ Contains all genetic information that is
    needed for reproduction and is essential
    for multiple cellular functions. ★
    """,
    """
                    ☆ Nucleolus ☆

    ★ The nucleolus is inside the nucleus and is
    concerned with producing and assembling
    the cell's ribosomes. ★
    """,
    """
                            ☆ Vacuole ☆

    ★ Specialized lysosomes. They take in and
    get rid of waste products. They also
    assist in cell structure. ★
    """
]

RANDOM_NOTE = random.choice(NOTES_INDEX)

class Snake:

    def __init__(self):
        self.body_size = BODY_PARTS
        self.coordinates = []
        self.squares = []

        for i in range(0, BODY_PARTS):
            self.coordinates.append([0, 0])

        for x, y in self.coordinates:
            square =  canvas.create_rectangle(x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill=SNAKE_COLOR, tag="snake")
            self.squares.append(square)

class Food:

    def __init__(self):

        x = random.randint(0, (GAME_WIDTH / SPACE_SIZE)-1) * SPACE_SIZE
        y = random.randint(0, (GAME_HEIGHT / SPACE_SIZE) - 1) * SPACE_SIZE

        self.coordinates = [x,y]

        canvas.create_rectangle(x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill=FOOD_COLOR, tag="food")

def next_turn(snake, food):

    x, y = snake.coordinates[0]

    if direction == "up":
        y -= SPACE_SIZE
    elif direction == "down":
        y += SPACE_SIZE
    elif direction == "left":
        x -= SPACE_SIZE
    elif direction == "right":
        x += SPACE_SIZE

    snake.coordinates.insert(0, (x, y))

    square = canvas.create_rectangle(x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill=SNAKE_COLOR)

    snake.squares.insert(0, square)

    if x == food.coordinates[0] and y == food.coordinates[1]:

        global score

        score += 1
        if DEBUG is True:
            print("[~] Debug: Increased the game score by +1")

        label.config(text="Score: {}".format(score))

        canvas.delete("food")

        food = Food()

    else:
        del snake.coordinates[-1]

        canvas.delete(snake.squares[-1])

        del snake.squares[-1]

    if check_collisions(snake):
        game_over()

    else:
        window.after(SPEED, next_turn, snake, food)

def change_direction(new_direction):

    global direction

    if new_direction == 'left':
        if direction != 'right':
          if direction != 'left':
            direction = new_direction
            if DEBUG is True:
              print("[~] Debug: User has changed direction to RIGHT")
    elif new_direction == 'right':
        if direction != 'left':
          if direction != 'right':
            direction = new_direction
            if DEBUG is True:
              print("[~] Debug: User has changed direction to LEFT")
    elif new_direction == 'up':
        if direction != 'down':
          if direction != 'up':
            direction = new_direction
            if DEBUG is True:
              print("[~] Debug: User has changed direction to UP")
    elif new_direction == 'down':
        if direction != 'up':
          if direction != 'down':
            direction = new_direction
            if DEBUG is True:
              print("[~] Debug: User has changed direction to DOWN")

def check_collisions(snake):

    x, y = snake.coordinates[0]

    if x < 0 or x >= GAME_WIDTH:
        return True
    elif y < 0 or y >= GAME_HEIGHT:
        return True

    for body_part in snake.coordinates[1:]:
        if x == body_part[0] and y == body_part[1]:
            if DEBUG is True:
                print("[~] Debug: User has game ended.")
            return True

    return False

def game_over():

    if DEBUG is True:
      print("[~] Debug: User has game ended.")
    time.sleep(1)
    canvas.delete(ALL)
    canvas.create_text(canvas.winfo_width()/2, canvas.winfo_height()/2, font=("Ariel", 70), text="Game Over", fill="red",tag="gameover")
    time.sleep(1)
    canvas.delete(ALL)
    canvas.create_text(canvas.winfo_width()/2.1, canvas.winfo_height()/2.1, font=("Ariel", 35), text=RANDOM_NOTE, fill="red",tag="endnotes")
    if DEBUG is True:
        if PRINT_NOTE_ON_GAME_END is True:
            print("[~] Debug: Printing notes when the game ends is enabled, so we are showing a random note.")
    if PRINT_NOTE_ON_GAME_END is True:
        print(RANDOM_NOTE)

window = Tk()
window.title("Snake v2")
window.resizable(False, False)

score = 0
direction = 'down'

label = Label(window, text="Score: {}".format(score), font=("Ariel", 40))
label.pack()

canvas = Canvas(window, bg=BACKGROUND_COLOR, height=GAME_HEIGHT, width=GAME_WIDTH)
canvas.pack()

window.update()

window_width = window.winfo_width()
window_height = window.winfo_height()
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

x = int((screen_width/2) - (window_width/2))
y = int((screen_height/2) - (window_height/2))

window.geometry(f"{window_width}x{window_height}+{x}+{y}")

window.bind('<Left>', lambda event: change_direction('left'))
window.bind('<Right>', lambda event: change_direction('right'))
window.bind('<Up>', lambda event: change_direction('up'))
window.bind('<Down>', lambda event: change_direction('down'))

snake = Snake()
food = Food()

next_turn(snake, food)

window.mainloop()
