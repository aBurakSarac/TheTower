import pygame as pg
#import os
#import shelve
VERSION =  "0.3.0"

# Initialize pygame modules
pg.font.init()
pg.mixer.init()

# Set up the dimensions
WIDTH, HEIGHT = 360, 640
WIN = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption(f"The Tower - {VERSION}")

BLOCK_HEIGHT = HEIGHT // 25
FLOOR_HEIGHT = HEIGHT//10
FINISH_LINE = pg.Rect(0, 20, WIDTH, 10)

# Define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 128, 0)
RED = (128,0,0)
SKY = (48, 172, 255)
BLOCK_COLOR = (232, 190, 172)

# Set the fixed values
FPS = 60
VEL = 6
# Set up the font for displaying text
PLAY_FONT1 = pg.font.SysFont("arial", 32)
PLAY_FONT2 = pg.font.SysFont("arial", 50)

MOVE_FORWARD = pg.USEREVENT + 1
MOVE_BACKWARDS = pg.USEREVENT + 2

def draw_window(floor, is_started,blocks, score):
    """
    Draw the game window with the floor and a start message if the game has not started yet.
    
    Args:
        floor (pygame.Rect): Rectangle representing the floor.
        is_started (bool): Flag indicating if the game has started or not.
    """
    WIN.fill(SKY)  # Fill the window with sky color
    pg.draw.rect(WIN, GREEN, floor)  # Draw the floor
    pg.draw.rect(WIN, RED, FINISH_LINE)
    if is_started == False:
        start_game()

    for block in blocks:
        pg.draw.rect(WIN, BLOCK_COLOR, block)
    
    draw_score(score)
    pg.display.update()


def start_game():
    draw_text = PLAY_FONT1.render("PRESS SPACE TO START", 1, WHITE)
    # If the game has not started yet, display the start message at the center of the window
    WIN.blit(draw_text, (WIDTH/2 - draw_text.get_width() / 2, HEIGHT/2 - draw_text.get_height()/2))

def draw_score(score):
    draw_score = PLAY_FONT1.render(str(score), 1, WHITE)
    WIN.blit(draw_score, (WIDTH - draw_score.get_width() - WIDTH / 20, HEIGHT / 20 + draw_score.get_height()/2))

def game_over(score):
    #save_score(score)
    #high_score = read_hi_score()
    draw_game_over = PLAY_FONT2.render("GAME OVER", 1, WHITE)
    draw_last_score = PLAY_FONT2.render("SCORE: " + str(score), 1, WHITE)
    #if(high_score >= score):
    #    draw_high_score = PLAY_FONT1.render("HIGH SCORE " + str(high_score), 1, WHITE)
    WIN.blit(draw_game_over, (WIDTH/2 - draw_game_over.get_width() / 2, HEIGHT/2 - draw_game_over.get_height()/2- draw_last_score.get_height()))
    WIN.blit(draw_last_score, (WIDTH/2 - draw_last_score.get_width() / 2, HEIGHT/2 - draw_last_score.get_height()/2))
    #WIN.blit(draw_high_score, (WIDTH/2 - draw_high_score.get_width() / 2, HEIGHT/2 - draw_high_score.get_height()/2 + draw_last_score.get_height()))
    pg.display.update()

def well_done(score):
    draw_well_done = PLAY_FONT2.render("WELL DONE", 1, WHITE)
    draw_last_score = PLAY_FONT2.render("SCORE: " + str(score), 1, WHITE)
    WIN.blit(draw_well_done, (WIDTH/2 - draw_well_done.get_width() / 2, HEIGHT/2 - draw_well_done.get_height()/2- draw_last_score.get_height()))
    WIN.blit(draw_last_score, (WIDTH/2 - draw_last_score.get_width() / 2, HEIGHT/2 - draw_last_score.get_height()/2))
    pg.display.update()

"""
def save_score(score):
    d = shelve.open('score.txt')
    if score > d['score']:
        d['score'] = score
    d.close()

def read_hi_score():
    d = shelve.open('score.txt')
    hi_score = d['score']
    print(hi_score)
    d.close()
    return hi_score
    """

def create_block(block_altitude, block_length,blocks):
    if(len(blocks) > 1):
        if blocks[-1].left < blocks[-2].left:
            blocks[-1] = pg.Rect(blocks[-2].x, blocks[-1].y, block_length, BLOCK_HEIGHT)
        elif blocks[-1].right > blocks[-2].right:
            blocks[-1] = pg.Rect(blocks[-1].x, blocks[-1].y, block_length, BLOCK_HEIGHT)
    new_block = pg.Rect(0, block_altitude, block_length, BLOCK_HEIGHT) 
    blocks.append(new_block)

def calculate_block_size(blocks):
    if blocks[-1].right >= blocks[-2].right:
        return blocks[-1].right - blocks[-2].right
    elif blocks[-1].left <= blocks[-2].left:
        return blocks[-2].left - blocks[-1].left    


def move_block(block_length,blocks, is_forward):
    """
    Update the state and position of the block.
    """
    if blocks[-1].x + block_length >= WIDTH:
        pg.event.post(pg.event.Event(MOVE_BACKWARDS))
    elif blocks[-1].x <= 0 and is_forward == False:
        pg.event.post(pg.event.Event(MOVE_FORWARD))
    
    if is_forward:
        blocks[-1].x += VEL
    else:
        blocks[-1].x -= VEL
    

def main():
    # Set up the game clock
    clock = pg.time.Clock()
    
    blocks=[]
    block_altitude = HEIGHT - FLOOR_HEIGHT - BLOCK_HEIGHT
    block_length =  WIDTH * 2 // 3

    run = True
    floor = pg.Rect(0, HEIGHT - FLOOR_HEIGHT, WIDTH, FLOOR_HEIGHT)  # Create a rectangle representing the floor
    is_started = False
    is_finished = False
    is_forward = True

    score = 0

    while run:
        clock.tick(FPS)  # Limit the game loop to a specific frame rate

        for event in pg.event.get():
            if event.type == pg.QUIT or event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE:
                run = False
                pg.quit()

            if event.type == pg.KEYDOWN and event.key == pg.K_SPACE:
                if is_started == False:
                    is_started = True
                
                if len(blocks) >= 2:
                    cut_size = calculate_block_size(blocks)
                    block_length -= cut_size
                    if (cut_size == 0):
                        score += WIDTH // 2
                    if block_length <= 0:
                        block_length = 0
                        is_finished = True
                        
                if not is_finished and len(blocks) >= 1:
                    score += block_length
                
                create_block(block_altitude, block_length, blocks)
                block_altitude -= BLOCK_HEIGHT
                

            if event.type == MOVE_FORWARD:
                is_forward = True
            elif event.type == MOVE_BACKWARDS:
                is_forward = False
                
        if is_started and not is_finished:
            move_block(block_length, blocks, is_forward)  # Update the block position and state

        if block_altitude <= 0:
            well_done(score)
            pg.time.delay(5000)
            break

        if is_finished:
            game_over(score)
            pg.time.delay(5000)
            break

        
        draw_window(floor, is_started, blocks, score)  # Draw the game window
    main()
        
        
if __name__ == "__main__":
    main()