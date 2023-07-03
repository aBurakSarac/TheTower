import pygame as pg
import os
#Version 0.1.1

# Initialize pygame modules
pg.font.init()
pg.mixer.init()

# Set up the window dimensions
WIDTH, HEIGHT = 500, 1000
WIN = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption("The Tower")

# Define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 128, 0)
SKY = (48, 172, 255)

# Set the frames per second and velocity of the block
FPS = 60
VEL = 8

# Set up the font for displaying text
PLAY_FONT = pg.font.SysFont("arial", 32)

def draw_window(floor, is_started, length = 100):
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

    pg.display.update()


def move_block():
    """
    Update the state and position of the block.
    """
    # TODO: Add the implementation for handling the block
    """
        1) Create new block.
        2) Move the block until the key is pressed.
        3) Call place_block().
    """
    pass

def place_block():
    """ 
        1) Compare with the block below.
        2) Cut if perfect timing is failed.
        3) Fix the position of the block.
        4) Increase score by the length of the block.
    """
    pass


def draw_score():
    """
    Draw the score on the screen.
    """
    # TODO: Add the implementation for drawing the score
    pass

def main():
    # Set up the game clock
    clock = pg.time.Clock()

    run = True
    floor = pg.Rect(0, 900, WIDTH, 100)  # Create a rectangle representing the floor
    is_started = False

    while run:
        clock.tick(FPS)  # Limit the game loop to a specific frame rate

        for event in pg.event.get():
            if event.type == pg.QUIT or event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE:
                run = False
                pg.quit()

            if event.type == pg.KEYDOWN and event.key == pg.K_SPACE:
                if is_started == True:
                    #TODO: place_block()
                    pass
                else:
                    is_started=True

                    
        draw_window(floor, is_started)  # Draw the game window
        move_block()  # Update the block position and state
        
if __name__ == "__main__":
    main()

 