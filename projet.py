import pygame
import time
from random import *

blue=(113,177,227)
white=(255,255,255)
red=(255,8,4)
pygame.init()
surfaceW=800
surfaceH=500
ipeitW=80
ipeitH=144
brakageW=300
brakageH=300


surface=pygame.display.set_mode((surfaceW,surfaceH))

pygame.display.set_caption(" ipeit save your life :p ")

horloge=pygame.time.Clock()

img=pygame.image.load('C:/Users/user/Desktop/frontoffice_logo.jpg')

img1=pygame.image.load("C:/Users/user/Desktop/ilo_stainless_knife_one.png")
def brakage (x_brakage,y_brakage):
    surface.blit(img1,(x_brakage,y_brakage))
def score(compte):
    police=pygame.font.Font("C:/Users/user/Downloads/BradBunR.ttf",16)
    texte=police.render("score:"+str(compte),True,red)
    surface.blit(texte,[10,0])
def rejoue () :
    for event in pygame.event.get([pygame.KEYDOWN,pygame.KEYUP,pygame.QUIT]):
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        elif event.type == pygame.KEYUP:
            continue
        return event.key
    return None

def gameOver():
    
   
    time.sleep(2)
    
    while rejoue()==None:
        horloge.tick()
    principale()

def ipeit(x,y,image):
    surface.blit(image,(x,y))
    
def principale():
    x=150
    y=200
    y_mouv=0
    x_brakage=surfaceW
    y_brakage=-270
    vitesse= 1
    scoreact=0
    game_over=False
    while not game_over:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                game_over=True
            if event.type == pygame.KEYDOWN :
                if event.key == pygame.K_UP:
                    y_mouv=-0.5
            if event.type == pygame.KEYUP :
                y_mouv=0.5
        
        y+=y_mouv
        surface.fill(blue)
        ipeit(x,y,img)
        
        brakage(x_brakage,y_brakage)
        
        score(scoreact)
        
        x_brakage-=vitesse
        
        if y>surfaceH-40  or y<-10 :
            gameOver()
        if 4<= scoreact<7:
            vitesse=2        
        if 7<= scoreact<20:
            vitesse=4
        
        if x+ipeitW>x_brakage :
            if y<y_brakage + brakageH -50 :
                if x -ipeitW < x_brakage+ brakageW -30 :
                    gameOver()
        
        if x_brakage<(-1*brakageW):
            x_brakage=surfaceW
            y_brakage=randint(-250,150)
        if x_brakage < (x-brakageW) < x_brakage+2*vitesse:
            scoreact=scoreact+1

        pygame.display.update()
        
        
        
        
principale()
pygame.quit()
quit()