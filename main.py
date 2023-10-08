import pygame as pyg

# screen
fps = pyg.time.Clock()

resolution = [1280, 720]
screen = pyg.display.set_mode((resolution[0], resolution[1]))


# others
running = True
while running:
    fps.tick(60)

    for event in pyg.event.get():
        if event.type == pyg.QUIT:
            running = False

    screen.fill("gray")
    
    pyg.display.set_caption(f"Duas noites com Eduardo | {int(fps.get_fps())} fps")
    pyg.display.flip()

pyg.quit()