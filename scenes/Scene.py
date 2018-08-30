import pygame
import sys
import random

class Scene:
    def __init__(self, screen: pygame.Surface, manager):
        self.screen = screen
        self.manager = manager
        self.colors = (random.randint(1,255), random.randint(1,255), random.randint(1,255))
        #player start dictionary of co'ords n,s,e,w
        self.spacebg = pygame.image.load('./assets/spacebg.gif')

    def handle_input(self):
        # for event in pygame.event.get(): #we always want to handle quit.
        #     if event.type == pygame.QUIT:
        #         sys.exit()
        #     if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
        #         sys.exit()
        pass

    def run(self):
        #self.handle_input()
        #self.screen.fill((self.colors))
        self.screen.blit(self.spacebg,(0,0))

    def next_scene(self):
        return Scene(self.screen, self.manager)
