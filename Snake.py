import pygame
import sys
from random import randint
from PIL import Image

pygame.init()

class Snake_head(pygame.sprite.Sprite):

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

        self.image = head_im
        self.rect = self.image.get_rect()
        self.rect.center = (win_size_x//2, win_size_y//2)

    def update(self):
        width,height = win_size_x,win_size_y

        self.rect.x += x_point
        self.rect.y += y_point
        if self.rect.left > width:
            self.rect.right = 0
        if self.rect.right < 0:
            self.rect.left = width
        if self.rect.top < 0:
            self.rect.bottom = height
        if self.rect.bottom > height:
            self.rect.top = 0

class Simple_food(pygame.sprite.Sprite):

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

        width,height = win_size_x,win_size_y

        self.image = sim_food_im
        self.rect = self.image.get_rect()
        self.rect.center = (randint(1,width), randint(1,height))

def Spawn_sim_food():
    sim_food = Simple_food()
    food_sprites.add(sim_food)


def Add_im_for_sprite(names):
    for name in names:
        im = Image.open(name)
        if names[name]["type"] is "back":
            size = (win_size_x//names[name]["divider"],win_size_y//names[name]["divider"])
        elif names[name]["type"] is "item":
            size = (item_size // names[name]["divider"],item_size // names[name]["divider"])
        im = im.resize(size)
        im.save(name)

def Names_con(dev,ty):
    return {"divider":dev, "type":ty}

win_size_x = 600
win_size_y = 600
item_size = win_size_x + win_size_y
head_size = item_size // 30
food_size = item_size // 35

names =  {"forest.jpg":Names_con(1,"back"), "head.png":Names_con(head_size,"item"), "sim_food.png":Names_con(food_size,"item")}
Add_im_for_sprite(names)

back_im = pygame.image.load("forest.jpg")
window = pygame.display.set_mode((win_size_x,win_size_y))

head_sprites = pygame.sprite.Group()
head_im = pygame.image.load('head.png')
head = Snake_head()
head_sprites.add(head)

food_sprites = pygame.sprite.Group()
sim_food_im = pygame.image.load('sim_food.png')
sim_food = Simple_food()

clock = pygame.time.Clock()
run_speed = (win_size_y+win_size_x)//21
spawn_food_speed = 10

x_point,y_point = 0,0


next_render_time = 0

while True:
    current_time = pygame.time.get_ticks()

    clock.tick(30)
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                x_point = 1
                y_point = 0
            if event.key == pygame.K_LEFT:
                x_point = -1
                y_point = 0
            if event.key == pygame.K_DOWN:
                x_point = 0
                y_point = 1
            if event.key == pygame.K_UP:
                x_point = 0
                y_point = -1
    if current_time >= next_render_time:
        Spawn_sim_food()
        next_render_time = current_time + 3000

    window.blit(back_im, (0, 0))

    head_sprites.draw(window)
    head_sprites.update()

    food_sprites.draw(window)
    food_sprites.update()

    pygame.display.flip()
