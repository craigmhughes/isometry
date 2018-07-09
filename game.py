import pygame
import world_props
import worlds


run = True

# Window Variables
win_w = 700
win_h = 700

win = pygame.display.set_mode((win_w, win_h))
current_biome = worlds.overWorld

pygame.init()

world = worlds.overWorld.render(current_biome)

def render_world():

    for tile_set in world:
        for tile in tile_set:
            win.blit(tile.background, (tile.x, tile.y - 48), (0, 0, tile.w, tile.h))


while run:
    pygame.display.update()
    win.fill((100, 175, 225))

    render_world()

    # Check controls
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False


pygame.quit()
