import pgzrun
import random

WIDTH = 800
HEIGHT = 600
CENTER_X = WIDTH / 2
CENTER_Y = HEIGHT / 2
CENTER = (CENTER_X,CENTER_Y)
FINAL_LEVEL = 6
START_SPEED = 10
CATS = ["blackcat","fakesusie","whitecat"]

game_over = False
game_complete = False
current_level = 1
animations = []
cats = []

def draw():
    screen.clear()
    screen.fill("white")

def update():
    pass

def get_option(extra_items):
    cats_to_create = ["susie"]
    for i in range(extra_items):
        random_option = random.choice(CATS)
        cats_to_create.append(random_option)
    return cats_to_create

def create_cat(cats_to_create):
    new_items = []
    for option in cats_to_create:
        item = Actor(option + "img")
        new_items.append(item)
    return new_items

def layout_cats(cats_to_layout):
    number_of_gaps = len(cats_to_layout) + 1
    gap_size = WIDTH / number_of_gaps
    random.shuffle(cats_to_layout)
    for index,cat in enumerate(cats_to_layout):
        new_x_pos = (index + 1) * gap_size
        cat.x = new_x_pos

def animate_cats(cats_to_animate):
    global animations
    for cat in cats_to_animate:
        duration = START_SPEED - current_level
        cat.anchor("center","bottom")
        animation = animate(cat,duration=duration,on_finished=handle_game_over,y = HEIGHT)
        animations.append(animation)
    
def handle_game_over():
    global game_over
    game_over = True

def on_mouse_down(pos):
    global cats, current_level
    for cat in cats:
        if cat.collidepoint(pos):
            if "susie" in cat.image:
                handle_game_complete()
            else:
                handle_game_over()

def handle_game_complete():
    global cats, current_level, animations, game_complete
    stop_animations(animations)
    if current_level == FINAL_LEVEL:
        game_complete = True
    else:
        current_level += 1
        cats = []
        animations = []

def stop_animations(animations_to_stop):
    for animation in animations_to_stop:
        if animation.running:
            animation.stop()


pgzrun.go()