import pygame as p


p.init()
screen = p.display.set_mode((400, 400))



YELLOW = (255, 255, 0)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

running = True
while running:
    for event in p.event.get():
        if event.type == p.QUIT:
            running = False



    p.draw.circle(screen, YELLOW, (200, 200), 100)
    p.draw.circle(screen, BLACK, (200, 200), 100, 2)



    p.draw.circle(screen, RED, (160, 185), 25)
    p.draw.circle(screen, BLACK, (160, 185), 12)

    p.draw.circle(screen, RED, (240, 185), 18)
    p.draw.circle(screen, BLACK, (240, 185), 7)


    p.draw.line(screen, BLACK, (100, 130), (180, 160), 10)

    p.draw.line(screen, BLACK, (300, 145), (210, 180), 12)


    p.draw.rect(screen, BLACK, (150, 260, 100, 15))

    p.display.flip()

p.quit()
