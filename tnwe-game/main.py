import pygame as pyg
from os import getcwd

pyg.init()
# pyg.font.init()

# directorys
directory = f"{getcwd()}\\tnwe-game\\src\\"

# screen
fps = pyg.time.Clock()

resolution = [1280, 720]
screen = pyg.display.set_mode((resolution[0], resolution[1]))

# images
background = pyg.image.load(f"{directory}\\images\\main_office.png")
background = pyg.transform.scale(background, (resolution[0], resolution[1]))

icon = pyg.image.load(f"{directory}\\images\\icon.jpg")
pyg.display.set_icon(icon)

# fonts
font_in_game_low = pyg.font.Font(f"{directory}\\fonts\\OCRAEXT.TTF", 20)
font_in_game_medium = pyg.font.Font(f"{directory}\\fonts\\OCRAEXT.TTF", 40)

# others
running = True
while running:
    fps.tick(60)

    time_text = font_in_game_medium.render("10:00PM", True, (255, 255, 255))
    night_text = font_in_game_low.render("night 1", True, (255, 255, 255))
    battery_text = font_in_game_low.render("power: 100%", True, (255, 255, 255))
    usage_text = font_in_game_low.render("usage-level: 0", True, (255, 255, 255))

    for event in pyg.event.get():
        if event.type == pyg.QUIT:
            running = False

    screen.blit(background, (0, 0))
    screen.blit(time_text, (1110, 25))
    screen.blit(night_text, (1185, 65))
    screen.blit(battery_text, (20, 600))
    screen.blit(usage_text, (20, 620))

    pyg.display.set_caption(f"Two night's with Eduardo | {int(fps.get_fps())} fps")
    pyg.display.flip()

pyg.quit()
# pyg.font.quit()