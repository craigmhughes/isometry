import pygame

tile_size = 98
tile_c = int(tile_size / 4)

bg_dir = 'assets/sprites/overworld_tiles/'
img_place = '/0.png'

# Beach tiles
shallow_beach = 'ts_beach-shallow0/straight/'
shallow_beach_curve_out = 'ts_beach-shallow0/curve_out/'
shallow_beach_curve_in = 'ts_beach-shallow0/curve_in/'
beach = bg_dir + 'ts_beach0/straight/'

beach_grass =  'ts_grass-beach0/straight/'
beach_grass_curve_in = 'ts_grass-beach0/curve_in/'
beach_grass_curve_out = 'ts_grass-beach0/curve_out/'

# Water tiles
water = 'ts_deep0/straight/'

mid_water = 'ts_shallow-deep0/straight/'
mid_water_curve_in = 'ts_shallow-deep0/curve_in/'
mid_water_curve_out = 'ts_shallow-deep0/curve_out/'

shallow_water = 'ts_shallow0/straight/'

# Grass tiles
grass = 'ts_grass0/straight/'

current_world = 0


class Tile:
    background = None
    w = tile_size
    h = tile_size
    x = 0
    y = 0
    degree = 45

    def __init__(self, bg, x, y, degree):
        self.x = x
        self.y = y
        deg = 45

        if degree == 0:
            deg = "45"
            self.degree = "45"
        if degree == 1:
            deg = "135"
            self.degree = "135"
        if degree == 2:
            deg = "235"
            self.degree = "235"
        if degree == 3:
            deg = "315"
            self.degree = "315"

        self.background = pygame.image.load(bg_dir + bg + deg + img_place)
        self.background = pygame.transform.scale(self.background, [self.w,self.h])