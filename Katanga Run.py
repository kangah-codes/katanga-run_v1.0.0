import pygame
import pygame._view
from pygame.locals import *
from required import Animation
import math


pygame.init()
import os
import random
import time
from random import *


def about():
    white = 255,255,255
    screen = pygame.display.set_mode((700, 400))
    font = pygame.font.SysFont("calibri", 30)
    ins = font.render("Press Esc to return,",True,(0,0,0))
    ins1 = font.render("Katanga Run Version 1.0,",True,(0,0,0))
    ins2 = font.render("This game was made by Raph(1Sci B)",True,(0,0,0))
    ins3 = font.render("Akangah(1G/A A)",True,(0,0,0))
    ins4 = font.render( "and Bassell(1Sci A)",True,(0,0,0))
    ins5 = font.render("Copyright v 1.0 2016 ",True,(0,0,0))

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == K_ESCAPE:
                    new()

        screen.fill(white)
        screen.blit(ins,(10,10))
        screen.blit(ins1,(10,50))
        screen.blit(ins2,(10,100))
        screen.blit(ins3,(10,150))
        screen.blit(ins4,(10,200))
        screen.blit(ins5,(10,250))
        pygame.display.update()




def new():
    white = 255, 255, 255
    screen = pygame.display.set_mode((700, 400))
    font = pygame.font.SysFont("calibri", 30)
    st = font.render("Press S to Start", True, (0, 0, 0))
    kt = font.render("KATANGA RUN",True,(0,0,0))
    q = font.render("Press Q to Quit", True, (0, 0, 0))
    av = font.render("Press A to show info",True,(0,0,0))
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == K_s:
                    main()
                if event.key == K_q:
                    exit()
                if event.key == K_a:
                    about()

        screen.fill(white)
        screen.blit(st, (280, 180))
        screen.blit(q, (280, 300))
        screen.blit(av,(280,230))
        screen.blit(kt,(280,20))
        pygame.display.update()
# Define the colors we will use in RGB format
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
size1 = 20
size2 = 2
ground=259

# Clock
clock = pygame.time.Clock()

# Set up display
screen = pygame.display.set_mode((700, 400))
start = True
pygame.display.set_caption("KATANGA RUN")




# Game Objects




def main():
    class Background():
        def __init__(self):
            self.background = pygame.image.load("bg1.jpg")
            self.x = 0
            self.y = 0
            self.speed = 300  # PPS

        def Obs(self):
            self.image = pygame.image.load("obs.jpg")
            self.x = 0
            self.y = 0
            self.speed = 100

        def input(self):
            pass

        def draw(self, screen):
            screen.blit(self.background, (self.x, self.y))
            if self.x < 0:
                # Calculating next background posn
                new_x = 700 - math.fabs(self.x)
                screen.blit(self.background, (new_x, self.y))

        def update(self, dt):
            # print self.speed
            self.x -= dt / 1000.0 * self.speed
            pass
            if self.x < -700:
                self.x = 0

    class Player(pygame.sprite.Sprite):
        def __init__(self, *groups):
            self.animation = Animation([
                'Sprites/Run (1).png',
                'Sprites/Run (2).png',
                'Sprites/Run (3).png',
                'Sprites/Run (4).png',
                'Sprites/Run (5).png',
                'Sprites/Run (6).png',
                'Sprites/Run (7).png',
                'Sprites/Run (8).png',
            ], 100, True)
            self.jumpSpeed = 130.0
            self.scale = .2
            self.isJumping = False
            self.isFalling = True
            self.y = ground
            self.gscore = 10
            self.glife = 20
            self.SCORE = pygame.font.SysFont("calibri", 32)
            #self.score = self.SCORE.render("Score:%s" % (self.gscore), True, (0, 0, 0))


        def input(self, key):
            print "Jumping=%s,falling=%s"%(self.isJumping,self.isFalling)
            if key == pygame.K_w and (not self.isJumping and not self.isFalling):
                self.isJumping = True

        def update(self, deltatime):
            self.score = self.SCORE.render("Score:%s" % (self.gscore), True, (0, 0, 0))
            self.life = self.SCORE.render("Life:%s"% (self.glife),True,(0,0,0))


            if not (self.isJumping or  self.isFalling):
                self.animation.update(deltatime)
            self.rect = self.animation.getScaledImage(self.scale).get_rect()
            self.mask = pygame.mask.from_surface(self.animation.getScaledImage(self.scale))

            self.rect.x = 200
            if self.y > ground:
                self.y = ground
                self.isFalling = False
                self.isJumping = False
            if self.y < ground - self.rect.height:
                self.isFalling = True
                self.isJumping = False
                #pygame.transform.rotate(self.animation, 360)

            if self.isJumping:
                self.y -= self.jumpSpeed * deltatime / 600.0
            elif self.isFalling:
                self.y += self.jumpSpeed * deltatime / 600.0

            self.rect.y = self.y

            if player.glife <= 0:
                #from Font import fmain
                player.fmain()
                pygame.time.wait((main),100000)


        def draw(self, screen):
            img = self.animation.getScaledImage(self.scale)
            img_rect = img.get_rect()
            screen.blit(self.score, (10, 10))
            screen.blit(self.life,(600,10))
            screen.blit(img, (200, self.y))
            #screen.blit(self.yscore,(20,20))

        def fmain(self):
            white = 255, 255, 255
            screen = pygame.display.set_mode((700, 400))
            background = pygame.image.load("bg.png")
            font = pygame.font.SysFont("calibri", 30)
            font1 = pygame.font.SysFont("comicsansms", 45)
            text = font.render("Start Game", True, (0, 0, 0))
            te_re = text.get_rect()
            text1 = font.render("About", True, (0, 0, 0))
            katanga = font1.render("Katanga Run!!!", True, (0, 0, 0))
            quit = font.render("Quit", True, (255, 0, 0))

            gmae = font.render("Game Over!, Press Esc to restart", True, (255, 0, 0))
            yscore = font.render("Your score is:%s" % (player.gscore), True, (0, 0, 0))

            texts = ([font.render("Start Game", True, (0, 0, 0)),
                      font.render("About", True, (0, 0, 0)),
                      font.render("Quit", True, (255, 0, 0))
                      ])
            while True:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        exit()
                    if event.type == pygame.KEYDOWN:
                        if event.key == K_ESCAPE:
                            main()

                screen.fill(WHITE)
                screen.blit(gmae, (200, 180))
                screen.blit(yscore,(200,240))
                pygame.display.update()

    class Base_Obstacle(pygame.sprite.Sprite):
        def __init__(self):
            pass

        def update(self, deltatime):
            pass

        def draw(self, screen):
            pass

    class Obstacle(pygame.sprite.Sprite):
        def __init__(self):
            self.animation = Animation([
                'traps/robot/hit_1.png',
                'traps/robot/hit_2.png',
                'traps/robot/hit_3.png',
                'traps/robot/hit_4.png',
                'traps/robot/hit_5.png',
                'traps/robot/hit_6.png',
                'traps/robot/hit_7.png',
            ], 150, True)
            self.scale = .3
            self.x, self.y = 700, 310
            self.speed = 200  # PPS

        def update(self, deltatime):
            self.animation.update(deltatime)
            self.rect = self.animation.getScaledImage(self.scale).get_rect()
            self.rect.x = self.x
            self.rect.y = self.y

            self.mask = pygame.mask.from_surface(self.animation.getScaledImage(self.scale))

            self.x -= deltatime / 1000.0 * self.speed
            if self.x < 0:
                list = [2000,1500,700,900]
                self.x = list[0 or 1 or 2 or 3]

        def draw(self, screen):
            img = self.animation.getScaledImage(self.scale)

            screen.blit(pygame.transform.scale(img, (int(img.get_rect().width * .9),
                                                     int(img.get_rect().height * .7))), (self.x, self.y - 10))
            self.animation.getScaledImage(self.scale).get_rect()

    class Coin(pygame.sprite.Sprite):
        def __init__(self):
            self.animation = Animation(["Sprites/coin/0.png","Sprites/coin/1.png"], 150, True)
            self.x, self.y = 500, 330
            self.speed = 100  # PPS
            self.scale = .5

        def update(self, deltatime):
            self.animation.update(deltatime)
            self.rect = self.animation.getScaledImage(self.scale).get_rect()
            self.rect.x = self.x
            self.rect.y = self.y
            self.x -= deltatime / 1000.0 * self.speed

            # scale(Surface, (width, height), DestSurface=None) -> Surface
            self.rect.x = self.x
            self.rect.y = self.y
            self.mask = pygame.mask.from_surface(self.animation.getScaledImage(self.scale))

            if self.x < 0:
                self.x = (2000)

        def draw(self, screen):
            img = self.animation.getScaledImage(self.scale)
            screen.blit(pygame.transform.scale(img, (int(img.get_rect().width * .9),
                                                     int(img.get_rect().height * .7))), (self.x, 330))

    class Snake(pygame.sprite.Sprite):
        def __init__(self):
            self.animation = Animation([
                "Sprites/idle/idle_1.png",
                "Sprites/idle/idle_2.png",
                "Sprites/idle/idle_3.png",
                "Sprites/idle/idle_4.png",
                "Sprites/idle/idle_5.png",
                "Sprites/idle/idle_6.png"
            ], 150, True)
            self.scale = .4
            self.x, self.y = 3000, 310
            self.speed = 200  # PPS

        def update(self, deltatime):
            self.animation.update(deltatime)
            self.rect = self.animation.getScaledImage(self.scale).get_rect()
            self.rect.x = self.x
            self.rect.y = self.y

            self.mask = pygame.mask.from_surface(self.animation.getScaledImage(self.scale))

            self.x -= deltatime / 1000.0 * self.speed
            if self.x < 0:
                list = [20000, 1500, 700, 5000]
                self.x = list[0 or 1 or 2 or 3]

        def draw(self, screen):
            img = self.animation.getScaledImage(self.scale)

            screen.blit(pygame.transform.scale(img, (int(img.get_rect().width * .9),
                                                     int(img.get_rect().height * .7))), (self.x, self.y - 10))
            self.animation.getScaledImage(self.scale).get_rect()
    class Base_Obstacle(pygame.sprite.Sprite):
        def __init__(self):
            pass
        def update(self, deltatime):
            pass

        def draw(self, screen):
            pass


    class Life_Powerup(pygame.sprite.Sprite):
        def __init__(self):
            self.image = pygame.image.load("life.png")
            self.x, self.y = 700, 335
            self.speed = 150
            self.scale = .3


        def update(self, deltatime):
            self.x -= deltatime / 1000.0 * self.speed
            self.rect = self.image.get_rect()
            self.rect.x = self.x
            self.rect.y = self.y
            self.mask = pygame.mask.from_surface(self.image)
            if self.x < 0:
                clist = [50,300,1000,2300]
                self.x = clist[3]

        def draw(self, screen):
            img = self.image
            # screen.blit(pygame.transform.scale(img, (int(img.get_rect().width),
            #                                          int(img.get_rect().height * .7))), (self.x, 310))
            screen.blit(self.image,(self.x,300))

    # class Snake(pygame.sprite.Sprite):
    #     def __init__(self):
    #         self.animation = Animation([""])







    player = Player()
    background = Background()
    ob = Obstacle()
    coin = Coin()
    life = Life_Powerup()
    snake = Snake()


    playerpos = [1, 1]
    # Draw Images

    # Main loop
    ab = coin.draw(screen)


    while start:
        # import Font

        fps = clock.tick(60)

        # Input
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit(0)
            if event.type == pygame.KEYDOWN:
                if event.key == K_w:
                    player.input(event.key)

        # UPdate
        background.update(fps)
        player.update(fps)
        ob.update(fps)
        coin.update(fps)
        life.update(fps)
        snake.update(fps)

        # if pygame.sprite.collide_rect(player, ob):
        #     player.gscore -=0.5
        #     print player.gscore
        if player.gscore <=0:
            screen.fill(WHITE)
        if player.glife == 0:
            screen.fill(WHITE)
        if pygame.sprite.collide_rect(player,coin):
            player.gscore+=10
        if pygame.sprite.collide_mask(player,ob):
            player.glife-= 1
        if pygame.sprite.collide_mask(player,coin):
            player.gscore+=1
        if pygame.sprite.collide_mask(player,life):
            player.glife+=1
        if pygame.sprite.collide_mask(player,snake):
            player.glife-=5


        ab=None

        # Draw
        screen.fill((0, 0, 0))
        background.draw(screen)
        player.draw(screen)
        ob.draw(screen)
        coin.draw(screen)
        life.draw(screen)
        snake.draw(screen)



        # Update
        pygame.display.update()







if __name__ == "__main__":
    pass
    #New_Game()
    #main()
    new()
