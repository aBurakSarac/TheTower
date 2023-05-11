import pygame as pg
import os
pg.font.init()
pg.mixer.init()

WIDTH, HEIGHT = 500, 1000
WIN = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption("The Tower")

#COLORS
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 128, 0)
SKY = (48, 172, 255)

FPS = 60 
VEL = 8 #SPEED OF BLOCK

PLAY_FONT = pg.font.SysFont("arial", 32)

def draw_window(floor, is_started): #VISUALIZATION OF ITEMS
    WIN.fill(SKY)
    pg.draw.rect(WIN,GREEN, floor)
    draw_text = PLAY_FONT.render("PRESS SPACE TO START", 1, WHITE)
    if is_started == False:
        WIN.blit(draw_text, (WIDTH/2 - draw_text.get_width() /
                         2, HEIGHT/2 - draw_text.get_height()/2))
    pg.display.update()
        

def handle_block(): #TODO
    pass

def draw_score(): #TODO
    pass

def main():
    clock = pg.time.Clock()
    run = True
    floor = pg.Rect(0, 900, WIDTH, 100)
    is_started = False
    #block = pg.Rect(0,800,256,100)
    

    while run:
        clock.tick(FPS)
        for event in pg.event.get():
            if event.type == pg.QUIT:
                run = False
                pg.quit()
            if event.type == pg.KEYDOWN: 
                if event.key == pg.K_SPACE and is_started == False:
                    is_started = True

        handle_block()    
        draw_window(floor, is_started)
        

if __name__ == "__main__":
    main()




