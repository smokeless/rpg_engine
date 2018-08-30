from helpers.Constants import *
from scenes.Scene import Scene
import random
import sys

import pygame


class SceneManager:
    def __init__(self, screen: pygame.Surface, player):
        self.screen = screen
        self.scene = Scene(screen, self)
        self.state = "RUNNING"
        self.player = player
        self.text = ''
        self.pages = 0

    def change_scene(self):
        print('Scene Change.')
        self.scene = self.scene.next_scene()

    def get_current_scene(self):
        return self.scene

    def check_player_exit(self):
        pass

    def run(self):
        keys = pygame.key.get_pressed()
        # for event in pygame.event.get(): #we always want to handle quit.
        #     if event.type == pygame.QUIT:
        #         sys.exit()
        #     if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
        #         sys.exit()
        #     if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE and self.state == "TEXT":
        #         self.pages = 0
        #     if not event:
        #         break


        if self.state == "RUNNING":
            for event in pygame.event.get():  # we always want to handle quit.
                if event.type == pygame.QUIT:
                    sys.exit()
                if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    sys.exit()
                if not event:
                    break
            if keys[pygame.K_RIGHT]:
                self.player.change_direction('e')
                self.player.walk(3, 0)
            if keys[pygame.K_LEFT]:
                self.player.change_direction('w')
                self.player.walk(-3, 0)
            if keys[pygame.K_DOWN]:
                self.player.change_direction('s')
                self.player.walk(0, 3)
                # player.y += 3
            if keys[pygame.K_UP]:
                self.player.change_direction('n')
                self.player.walk(0, -3)
                # player.y -= 3
            if keys[pygame.K_r]:
                print('present text.')
                self.present_text('Howdy. This is some long ass text that will mess this up and now we are')

        self.scene.run()
        self.player.update()

        if self.state == "TEXT":
            self._present_text()
            #todo maybe refactor these cause DRY
            for event in pygame.event.get():  # we always want to handle quit.
                if event.type == pygame.QUIT:
                    sys.exit()
                if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    sys.exit()
                if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE and self.state == "TEXT":
                    self.pages = 0
                if not event:
                    break
            if keys[pygame.K_SPACE]:
                self.pages -= 1
                print(len(self.text))


    def switch_state(self, state):
        '''
        Switch state. Current states:
        RUNNING, everything runs normally.
        TEXT, presenting text. freeze the game, handle text.
        :param state:
        :return:
        '''
        self.state = state


    def present_text(self, text):
        self.text = text
        self.pages = len(text) * 30 #this is temporary, so hacky
        self.state = "TEXT"

    def _present_text(self):
        print(self.pages)
        pygame.font.init()
        font = pygame.font.get_default_font()
        font = pygame.font.SysFont(font, 30)
        text_surface = font.render(self.text, False, (255,255,255))
        font_x = 20
        font_y = SCREEN_HEIGHT / 2 + 20


        if self.pages != 0:
            border = pygame.draw.rect(self.screen, (0, 0, 255),
                         (0, SCREEN_HEIGHT / 2, SCREEN_WIDTH, SCREEN_HEIGHT / 2), 0)
            text = pygame.draw.rect(self.screen, (255, 255, 255),
                         (0, SCREEN_HEIGHT / 2, SCREEN_WIDTH, SCREEN_HEIGHT / 2), 10)
            self.screen.blit(text_surface, (font_x, font_y))

        else:
            self.state = "RUNNING"
