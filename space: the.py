import pygame
from scene_manager.SceneManager import SceneManager
from helpers.Constants import *
from living.Player import Player

if __name__ == "__main__":
    rect_x = 20
    rect_y = 20
    size = (RESOLUTION)
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("Space: The...")
    player = Player(screen)
    manager = SceneManager(screen, player)
    clock = pygame.time.Clock()
    # while True:
    #     keys = pygame.key.get_pressed()
    #     if keys[pygame.K_RIGHT]:
    #         player.change_direction('e')
    #         player.walk(3,0)
    #     if keys[pygame.K_LEFT]:
    #         player.change_direction('w')
    #         player.walk(-3,0)
    #     if keys[pygame.K_DOWN]:
    #         player.change_direction('s')
    #         player.walk(0,3)
    #         #player.y += 3
    #     if keys[pygame.K_UP]:
    #         player.change_direction('n')
    #         player.walk(0,-3)
    #         #player.y -= 3
    #     if keys[pygame.K_r]:
    #         manager.present_text('Some text.')
    while True:
        clock.tick(30)
        manager.run()
        #pygame.draw.rect(screen, (0, 255, 0), (rect_x, rect_y, 20, 20), 0)
        #if rect_x < WEST:
            #manager.change_scene()
        #player.update()
        #screen.blit(player.north_two, [200,200])

        pygame.display.flip()
