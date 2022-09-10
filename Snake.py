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

class Tail(pygame.sprite.Sprite):

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.Surface(())
        self.rect = self.image.get_rect()



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

def Spawn_Snake():
    global head
    head = Snake_head()
    all_sprites.add(head)

def Score_Update():
    global text_score
    text_score = score_font.render(f'Score: {score}', False, (255, 0, 0))

def Add_im_for_sprite(names):
    for name in names:

        bef_im = rf"im_sprites\{str(name)}"
        aft_im= rf"im_sprites_player_change\{str(name)}"

        im = Image.open(bef_im)
        if names[name]["type"] == "back":
            size = (win_size_x//names[name]["divider"],win_size_y//names[name]["divider"])
        elif names[name]["type"] == "item":
            size = (item_size // names[name]["divider"],item_size // names[name]["divider"])
        im = im.resize(size)
        im.save(aft_im)

def Names_con(dev,typ):
    return {"divider":dev, "type":typ}

win_size_x = 600
win_size_y = 600
FPS = 30
score = 0
run_speed = 2
sim_food_time_delay = 5000
sim_food_time_delay_part = 0

item_size = win_size_x + win_size_y
head_size = item_size // 30
food_size = item_size // 35
score_font_size = int(win_size_x*0.05)

score_font = pygame.font.SysFont('Comic Sans MS', score_font_size)

text_score = None
head = None

names =  {"forest.jpg":Names_con(1,"back"), "head.png":Names_con(head_size,"item"), "sim_food.png":Names_con(food_size,"item")}
Add_im_for_sprite(names)

back_im = pygame.image.load("im_sprites_player_change\\forest.jpg")
head_ic = pygame.image.load('im_sprites\\head.png')
head_im = pygame.image.load("im_sprites_player_change\\head.png")
sim_food_im = pygame.image.load('im_sprites_player_change\\sim_food.png')

window = pygame.display.set_mode((win_size_x,win_size_y))
pygame.display.set_caption('Uchi_snake')
pygame.display.set_icon(head_ic)

all_sprites = pygame.sprite.Group()
food_sprites = pygame.sprite.Group()

clock = pygame.time.Clock()
spawn_food_speed = 10

x_point,y_point = 0,0

sim_food_time = 0

Spawn_Snake()
Score_Update()

while True:
    current_time = pygame.time.get_ticks()

    clock.tick(FPS)

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:
            match event.key:
                case pygame.K_RIGHT:
                    x_point = run_speed
                    y_point = 0
                case pygame.K_LEFT:
                    x_point = -run_speed
                    y_point = 0
                case pygame.K_DOWN:
                    x_point = 0
                    y_point = run_speed
                case pygame.K_UP:
                    x_point = 0
                    y_point = -run_speed

    if current_time >= sim_food_time:
        Spawn_sim_food()
        sim_food_time = current_time + sim_food_time_delay - 0.5*sim_food_time_delay_part

    window.blit(back_im, (0, 0))
    window.blit(text_score, (0, 0))

    all_sprites.update()
    food_sprites.update()

    eat = pygame.sprite.spritecollide(head,food_sprites,True)
    if eat:
        score += 1
        if score%7 == 0:
            run_speed +=1
            sim_food_time_delay_part += 500 + 0.5*sim_food_time_delay_part
        Score_Update()
        window.blit(text_score, (0, 0))


    all_sprites.draw(window)
    food_sprites.draw(window)
    pygame.display.flip()
