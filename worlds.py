import pygame

import world_props

tile_c = int(world_props.tile_c)

def switch_tile(ground, num, tile, degree):
    bg_dir = 'assets/sprites/overworld_tiles/'
    img_place = '/0.png'

    if degree == 0:
        ground[num].degree = "45"
    if degree == 1:
        ground[num].degree = "135"
    if degree == 2:
        ground[num].degree = "235"
    if degree == 3:
        ground[num].degree = "315"

    ground[num].background = pygame.image.load(bg_dir + tile + ground[num].degree + img_place)
    ground[num].background = pygame.transform.scale(ground[num].background, [ground[num].w, ground[num].h])


# Must build from top right to bottom left
class overWorld:
    x_offset = 25
    y_offset = 0

    def adj_xy(self, x, y):
        self.x_offset = x
        self.y_offset = y

    # Builds Ground
    def build_base(self, ground, chosen_tile):
        rendered = False
        ren_num = 0
        y_off = 0
        x_off = 25
        bounds = [2, 6, 12, 20, 30, 42, 56, 71, 87, 103, 119, 135, 151, 167, 183, 199, 213, 224, 233, 240, 245, 248]

        while not rendered:
            if not(ren_num >= bounds[len(bounds) - 1]):
                if ren_num in bounds:

                    if ren_num >= bounds[6]:
                        if y_off == 0:
                            y_off = 1
                            x_off = -1
                        elif y_off == 1:
                            y_off = 2
                            x_off = -3
                        else:
                            y_off += 2
                            x_off = -3
                    else:
                        x_off -= 4

                    self.adj_xy(self, x_off, y_off)

                ground.append(world_props.Tile(chosen_tile, tile_c * self.x_offset, tile_c * (self.y_offset - 1), 0))

                ren_num += 1
                self.y_offset += 1
                self.x_offset += 2
            else:
                rendered = True

        self.ground_changes(self, ground)

        return

    def ground_changes(self, ground):

        if world_props.current_world == 0:
            count = 0
            while count < 6:
                switch_tile(ground, 30 + count, world_props.water, 0)
                count += 1

    def render(self):
        if world_props.current_world == 0:
            return [self.get_ground(self)]

    def get_ground(self):
        ground = []

        chosen_tile = world_props.grass

        if world_props.current_world == 0:
                self.build_base(self, ground, chosen_tile)

        return ground

    def __init__(self):
        pass
