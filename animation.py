import pygame



#class for explosion
class Explosion(pygame.sprite.Sprite):
    def __init__(self, x, y, size):
        pygame.sprite.Sprite.__init__(self)
        self.images = []
        for eps in range(1,6):
            #load explosion image
            img = pygame.image.load(f'./image/exp{eps}.png')
            #explosion size
            if size == 1:
                img = pygame.transform.scale(img, (20, 20))
            elif size == 2:
                img = pygame.transform.scale(img, (40, 40))
            elif size == 3:
                img = pygame.transform.scale(img, (160, 160))
            elif size == None:
                img = pygame.transform.scale(img, (400, 400))
            #append the img into list
            self.images.append(img)
        self.index = 0
        self.image = self.images[self.index]
        self.rect = self.image.get_rect()
        self.rect.center = [x,y]
        self.counter = 0

    
    def update(self):
        explosion_speed = 3
        self.counter += 1

        if self.counter >= explosion_speed and self.index < len(self.images) - 1:
            self.counter = 0
            self.index += 1
            self.image = self.images[self.index]

        if self.index >= len(self.images) - 1 and self.counter >= explosion_speed:
            self.kill()

    
    def sprite_groups():
        Explosion_group = pygame.sprite.Group()
        return Explosion_group
        
