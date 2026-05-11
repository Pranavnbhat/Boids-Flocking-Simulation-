import pygame 
import math 
import random 
from sys import exit
from pygame.math import Vector2 as vec


class Boid(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        
        self.side = 15
        self.h = math.sqrt(3)/2 * self.side
        
        self.image= pygame.Surface((self.side, int(self.h)), pygame.SRCALPHA)
        
        points = [
            (self.side/2, 0),        # top
            (0, self.h),             # bottom left
            (self.side, self.h)           # bottom right
        ]

        pygame.draw.polygon(self.image, (255, 255, 255), points)
        self.rect = self.image.get_rect(center=(400, 300))

        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        pygame.init()
        screen = pygame.display.set_mode((800,600))
        pygame.display.set_caption('Boids')
        clock = pygame.time.Clock()
        
        
        
        
        
        
        while True: 
            screen.fill(206,255,255)
            
            
            
            
            
            
            
            
            pygame.display.update()
            clock.tick(60)