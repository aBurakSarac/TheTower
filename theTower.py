import pygame as pg
import os
#Version 0.1.1

# Initialize pygame modules
pg.font.init()
pg.mixer.init()

# Set up the dimensions
WIDTH, HEIGHT = 360, 640
WIN = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption("The Tower")

BLOCK_HEIGHT = HEIGHT // 25
FLOOR_HEIGHT = HEIGHT//10

# Define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 128, 0)
SKY = (48, 172, 255)
BLOCK_COLOR = (232, 190, 172)

# Set the fixed values
FPS = 60
VEL = 4
# Set up the font for displaying text
PLAY_FONT = pg.font.SysFont("arial", 32)

MOVE_FORWARD = pg.USEREVENT + 1
MOVE_BACKWARDS = pg.USEREVENT + 2

def draw_window(floor, is_started,blocks):
    """
    Draw the game window with the floor and a start message if the game has not started yet.
    
    Args:
        floor (pygame.Rect): Rectangle representing the floor.
        is_started (bool): Flag indicating if the game has started or not.
    """
    WIN.fill(SKY)  # Fill the window with sky color
    pg.draw.rect(WIN, GREEN, floor)  # Draw the floor
    if is_started == False:
        draw_text = PLAY_FONT.render("PRESS SPACE TO START", 1, WHITE)
        # If the game has not started yet, display the start message at the center of the window
        WIN.blit(draw_text, (WIDTH/2 - draw_text.get_width() / 2, HEIGHT/2 - draw_text.get_height()/2))
    
    for block in blocks:
        pg.draw.rect(WIN, BLOCK_COLOR, block)

    pg.display.update()

def create_block(block_altitude, block_length,blocks):
    """
    if [-1].right > [-2].right:
        length -= right - [-2].right

    if [-1].x < [-2].x:
        length = [-2].right - [-1].x
    else:
        length = [-1].x + length - [-2].x
    
    [-1].x
    [-1].x + length
    [-2].x
    [-2].x + length
    """
    """
    new_block = pg.Rect(0, block_altitude, block_length, BLOCK_HEIGHT)
    if len(blocks) >= 1:
        if new_block.right > blocks[-1].right:
            block_length -= new_block.right - blocks[-1].right
        elif new_block.left < blocks[-1].left:
            block_length -= blocks[-1].left - new_block.left
    """
    new_block = pg.Rect(0, block_altitude, block_length, BLOCK_HEIGHT)
    print("Block Length: " + str(block_length))
    blocks.append(new_block)


def move_block(block_altitude, block_length,blocks, is_forward):
    """
    Update the state and position of the block.
    """
    # TODO: Add the implementation for handling the block
    """
        1) Create new block.
        2) Move the block until the key is pressed.
    """
    if blocks[-1].x + block_length >= WIDTH:
        pg.event.post(pg.event.Event(MOVE_BACKWARDS))
    elif blocks[-1].x <= 0 and is_forward == False:
        pg.event.post(pg.event.Event(MOVE_FORWARD))
    
    if is_forward:
        blocks[-1].x += VEL
    else:
        blocks[-1].x -= VEL


def draw_score():
    """
    Draw the score on the screen.
    """
    # TODO: Add the implementation for drawing the score
    pass

def main():
    # Set up the game clock
    clock = pg.time.Clock()
    
    blocks=[]
    block_altitude, block_length = HEIGHT - FLOOR_HEIGHT - BLOCK_HEIGHT, WIDTH // 2
    run = True
    floor = pg.Rect(0, HEIGHT - FLOOR_HEIGHT, WIDTH, FLOOR_HEIGHT)  # Create a rectangle representing the floor
    is_started = False
    is_forward = True

    while run:
        clock.tick(FPS)  # Limit the game loop to a specific frame rate

        for event in pg.event.get():
            if event.type == pg.QUIT or event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE:
                run = False
                pg.quit()

            if event.type == pg.KEYDOWN and event.key == pg.K_SPACE:
                if is_started == False:
                    is_started = True
                create_block(block_altitude, block_length, blocks)
                block_altitude -= BLOCK_HEIGHT

            if event.type == MOVE_FORWARD:
                is_forward = True
            elif event.type == MOVE_BACKWARDS:
                is_forward = False
                
        if is_started:
            move_block(block_altitude, block_length, blocks, is_forward)  # Update the block position and state
        
        draw_window(floor, is_started, blocks)  # Draw the game window

        if block_length <= 0:
            pg.quit()
        
        
if __name__ == "__main__":
    main()