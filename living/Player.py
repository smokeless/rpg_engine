import pygame
from helpers.SpriteSheet import SpriteSheet

class Player(pygame.sprite.Sprite):
    def __init__(self, screen):
        #each image chunk x is 24 y is 32
        pygame.sprite.Sprite.__init__(self)
        COLOR_KEY = (32, 156, 0)
        IMAGE_X = 24
        IMAGE_Y = 32

        self.screen = screen
        self.sheet = SpriteSheet('./assets/living/player.png')

        #get north images
        self.north_one = self.sheet.get_image(0, 0, IMAGE_X, IMAGE_Y, COLOR_KEY)
        self.north_two = self.sheet.get_image(24, 0, IMAGE_X, IMAGE_Y, COLOR_KEY)
        self.north_three = self.sheet.get_image(48, 0, IMAGE_X, IMAGE_Y, COLOR_KEY)
        self.north_anim = [self.north_one, self.north_two, self.north_three]

        #get east images
        self.east_one = self.sheet.get_image(0, 32, IMAGE_X, IMAGE_Y, COLOR_KEY)
        self.east_two = self.sheet.get_image(24, 32, IMAGE_X, IMAGE_Y, COLOR_KEY)
        self.east_three = self.sheet.get_image(48, 32, IMAGE_X, IMAGE_Y, COLOR_KEY)
        self.east_anim = [self.east_one, self.east_two, self.east_three]

        #get south images
        self.south_one = self.sheet.get_image(0, 64, IMAGE_X, IMAGE_Y, COLOR_KEY)
        self.south_two = self.sheet.get_image(24, 64, IMAGE_X, IMAGE_Y, COLOR_KEY)
        self.south_three = self.sheet.get_image(48, 64, IMAGE_X, IMAGE_Y, COLOR_KEY)
        self.south_anim = [self.south_one, self.south_two, self.south_three]

        #get west images
        self.west_one = self.sheet.get_image(0, 96, IMAGE_X, IMAGE_Y, COLOR_KEY)
        self.west_two = self.sheet.get_image(24, 96, IMAGE_X, IMAGE_Y, COLOR_KEY)
        self.west_three = self.sheet.get_image(48, 96, IMAGE_X, IMAGE_Y, COLOR_KEY)
        self.west_anim = [self.west_one, self.west_two, self.west_three]

        self.direction = 'n'
        self.image = self.north_one
        self.rect = self.north_one.get_rect()
        self.x = 100
        self.y = 100

    def walk(self, x, y):
        self.x += x
        self.y += y


    def update(self, *args):
        y_image = self.y // 3 % 3
        x_image = self.x // 3 % 3
        if self.direction == 'n':
            self.image = self.north_anim[y_image]

        if self.direction == 'e':
            self.image = self.east_anim[x_image]

        if self.direction == 's':
            self.image = self.south_anim[y_image]

        if self.direction == 'w':
            self.image = self.west_anim[x_image]

        self.screen.blit(self.image, [self.x, self.y])

    def change_direction(self, direction: str ):
        self.direction = direction
        self.moving = True

    def stop(self):
        self.moving = False
        self.image = self.north_two
        print('stop called {}'.format(self.moving))
