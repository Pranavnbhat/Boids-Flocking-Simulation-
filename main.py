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
        self.velocity = vec(random.choice([3,2-1,1,2,3]), random.choice([3,2-1,1,2,3]))
        
        self.max_speed = 4
        
        
        
        self.perception_radius = 100 

        points = [        
            (self.side/2, 0),        # top        
            (0, self.h),             # bottom left        
            (self.side, self.h)      # bottom right        
        ]        
        
        pygame.draw.polygon(self.image, (0, 0, 0), points)    

        
        
        


    
        
        
    

                
    
    def seperation(self,Boidgroup):
        steering = vec(0, 0)
        for Boid in Boidgroup:
            if Boid!= self:
                distance=(self.vec - Boid.vec).length()
                if distance<self.perception_radius and distance>0:
                    diff = self.vec - Boid.vec 
                    diff = diff.normalize() / distance
                    steering += diff
                    
        return steering                
        
    def alignment (self,Boidgroup):
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
            return avg_pos-self.vec
        return vec(0, 0)  # no neighbours, no force    
        
        
    #def barrier(self):
        #if self.rect.centerx<some value near 0:
            #self.velocity +=some positive value 
        #if self.rect.centerx<some value near 800: 
            #self.velocity +=some negative value  

        #similiar for y 
    
    def barrier(self):
        margin = 50
        turn_factor = 0.5
    
        if self.rect.centerx < margin:
            self.velocity.x += turn_factor
        if self.rect.centerx > 800 - margin:
            self.velocity.x -= turn_factor
        if self.rect.centery < margin:
            self.velocity.y += turn_factor
        if self.rect.centery > 600 - margin:
            self.velocity.y -= turn_factor    
        
        
        
        
        
        
        
        
        
    def update(self, Boidgroup,x,y,z):
        sep = self.seperation(Boidgroup)
        ali = self.alignment(Boidgroup)
        coh = self.cohesion(Boidgroup)    
        
        self.velocity += sep * (0.04+(0.01*z))
        self.velocity += ali * (0.04+(0.01*x))
        self.velocity += coh * (0.04+(0.01*y))
        
        self.barrier()
        
        if self.velocity.length() > self.max_speed:
            self.velocity = self.velocity.normalize() * self.max_speed
        
        self.vec += self.velocity
        self.rect.center = (int(self.vec.x), int(self.vec.y))
        
        
        
        
     
 
pygame.init()
screen = pygame.display.set_mode((800,600))
pygame.display.set_caption('Boids')
clock = pygame.time.Clock() 

buffer_timer=pygame.USEREVENT + 1
buffer_state=False 



Boidgroup= pygame.sprite.Group()
    
        
        
    
x, y, z = 0, 0, 0 
input_text = ""
input_active = False
font_input = pygame.font.SysFont(None, 30)       
        

        
        
while True: 
    screen.fill((206,255,255))

    for event in pygame.event.get():
        if event.type==pygame.QUIT:        
            pygame.quit()        
            exit()
            
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_i:
                input_active = True
                input_text = ""
            elif input_active:
                if event.key == pygame.K_RETURN:
                    parts = input_text.split()
                    if len(parts) == 3:
                        try:
                            x, y, z = map(float, parts)
                        except:
                            pass 
                        input_active = False  
                        input_text = ""
                elif event.key == pygame.K_BACKSPACE:
                    input_text = input_text[:-1]
                else:
                    input_text += event.unicode 
    
        if event.type ==pygame.MOUSEBUTTONDOWN and not buffer_state:
            buffer_state=True
            mousepos = pygame.mouse.get_pos()
            Boidgroup.add(Boid(mousepos[0], mousepos[1]))
        
        
        if buffer_state:
            pygame.time.set_timer(buffer_timer, 10)    # change x to however long buffer should be 
            if event.type ==buffer_timer:
                buffer_state= False 
            
    if input_active:
        pygame.draw.rect(screen, (255,255,255), (10, 10, 300, 30))
        txt = font_input.render(input_text, True, (0,0,0))
        screen.blit(txt, (15, 15)) 
    else:
        #pygame.draw.rect(screen, (255,255,255), (10, 10, 300, 30))    
        message= 'Press the key "i" to input values'         
        txt = font_input.render(message, True, (0,0,0))        
        screen.blit(txt, (15, 15))        
               
    vals = font_input.render(f"Ali:{x}  Coh:{y}  Sep:{z}", True, (0,0,0))
    screen.blit(vals, (15, 570))



    
                        
                
    
            

    
    Boidgroup.update(Boidgroup,x,y,z)
    Boidgroup.draw(screen)
            
                        
            
            
    pygame.display.update()
    clock.tick(60)                  