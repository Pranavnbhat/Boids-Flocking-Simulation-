import pygame 
import math 
import random 
from sys import exit
from pygame.math import Vector2 as vec


class Boid(pygame.sprite.Sprite):
    def __init__(self,x,y):
        super().__init__()
        
        self.side = 15        
        self.h = math.sqrt(3)/2 * self.side        
        
        self.image= pygame.Surface((self.side, int(self.h)), pygame.SRCALPHA) 
        
        
        self.rect = self.image.get_rect(center=(x, y))
        
        self.vec=vec(self.rect.centerx,self.rect.centery)
        self.velocity = vec(random.randint(-3,3), random.randint(-3,3))
        
        self.max_speed = 4
        
        
        
        self.perception_radius = 50 

        points = [        
            (self.side/2, 0),        # top        
            (0, self.h),             # bottom left        
            (self.side, self.h)      # bottom right        
        ]        
        
        pygame.draw.polygon(self.image, (255, 255, 255), points)    

        
        
        


    
        
        
    

                
    
    def seperation(self,Boidgroup):
        steering = vec(0, 0)
        for Boid in Boidgroup:
            if Boid!= self:
                distance=(self.vec - Boid.vec).length()
                if distance<self.perception_radius:
                    diff = self.vec - Boid.vec 
                    diff = diff.normalize() / distance
                    steering += diff
                    
        return steering                
        
    def alignement(self,Boidgroup):
        avg_velocity=vec(0,0)
        count=0
        for Boid in Boidgroup:
            if Boid!= self:
                distance=(self.vec - Boid.vec).length()
                if distance<self.perception_radius:
                    avg_velocity=avg_velocity+Boid.velocity
                    count += 1
        if count > 0:
            avg_velocity /= count 
        return avg_velocity    
    
    
    def cohesion(self,Boidgroup):
        avg_pos=vec(0,0)
        count=0
        for Boid in Boidgroup:
            if Boid!= self:
                distance=(self.vec - Boid.vec).length()
                if distance<self.perception_radius:
                    avg_pos += Boid.vec 
                    count += 1
        if count >0:
            avg_pos /= count 
        return avg_pos
                 
        
        
        
        
        
        
        
        
        
    def update(self, Boidgroup):
        sep = self.separation(Boidgroup)
        ali = self.alignment(Boidgroup)
        coh = self.cohesion(Boidgroup)    
        
        self.velocity += sep * 0.05
        self.velocity += ali * 0.05
        self.velocity += coh * 0.05
        
        
       self.vec += self.velocity
       self.rect.center = (int(self.vec.x), int(self.vec.y))

        
 
pygame.init()
screen = pygame.display.set_mode((800,600))
pygame.display.set_caption('Boids')
clock = pygame.time.Clock() 
            
        
        
        
        
        
        
while True: 
    screen.fill((206,255,255))
            
    for event in pygame.event.get():
        if event.type==pygame.QUIT:        
            pygame.quit()        
            exit()        
            
            
    pygame.display.update()
    clock.tick(60)                  