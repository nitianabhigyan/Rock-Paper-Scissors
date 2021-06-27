import random
import pygame
from time import sleep
from pygame.locals import * #hwsurface is defined here
import threading

pygame.init()
#width = (pygame.display.Info().current_w -105)
#height = (pygame.display.Info().current_h -85)
width = (pygame.display.Info().current_w)
height = (pygame.display.Info().current_h)


gamefont = pygame.font.Font('go3v2.ttf',32)
#gameDisplay = pygame.display.set_mode((width,height))
gameDisplay = pygame.display.set_mode((width,height),HWSURFACE|DOUBLEBUF|RESIZABLE)
pygame.display.set_caption('Rock Paper Scissors')


#colours
black = (0,0,0)
white = (255,255,255)
green = (124,252,0)
blue = (0,0,135)
yellow = (255,251,66)
hotpink = (255,105,180)
red = (230,0,0)
dark_green = (0,102,0)
orange = (255, 102, 0)
refresh_rate= .15


def loading_Screen(y):
    refresh_rate= y
    d1 = width * .4
    d2 = height  * .4
    alph = 0
    for i in range(0,5):
        #1st
        paperimg = pygame.image.load('loading/tile000.png')
        gameDisplay.blit(paperimg,(d1,d2))
        display_text('Loading',black,d1+162,d2+220)
        #2nd
        paperimg = pygame.image.load('loading/tile001.png')
        gameDisplay.blit(paperimg,(d1,d2))
        display_text('Loading.',black,d1+162,d2+220)
        #3rd
        paperimg = pygame.image.load('loading/tile002.png')
        gameDisplay.blit(paperimg,(d1,d2))
        display_text('Loading..',black,d1+162,d2+220)
        #4th
        paperimg = pygame.image.load('loading/tile003.png')
        gameDisplay.blit(paperimg,(d1,d2))
        display_text('Loading...',black,d1+162,d2+220)
    #logic for fading out
    sleep(.2) # for music 
    pygame.mixer.music.load('music/welcome.mp3')
    pygame.mixer.music.play(0)
    for alph in range (255,0,-1):
        gameDisplay.fill((alph,alph,alph))
        pygame.display.update()
        static_display('...Welcome...',height/2,(255-alph,255-alph,255-alph))
        #sleep(.01)
    sleep(1.2)
    #pygame.mixer.fadeout(3) this is not working
    pygame.mixer.music.stop()
    
    
def exit_Screen():
    #1st
    refresh_rate = .2
    d1 = width * .34
    d2 = height  * .35
    paperimg0 = pygame.image.load('exiting/0.gif')
    paperimg1 = pygame.image.load('exiting/1.gif')
    pygame.mixer.music.load('music/ending.mp3')
    pygame.mixer.music.play(-1)
    # for end display
    text = "Thank you for playing "
    static_display(text,50,hotpink)
    for i in range (0,7):
        gameDisplay.blit(paperimg0,(d1,d2))
        pygame.display.flip()
        sleep(refresh_rate)
        #2nd
        gameDisplay.blit(paperimg1,(d1,d2))        
        pygame.display.flip()
        sleep(refresh_rate)
        
    for alph in range (255,0,-1):
        gameDisplay.fill((alph,alph,alph))
        static_display(' .:Made By:. ',height/2 - 16,(255-alph,255-alph,255-alph))
        static_display('Abhigyan Kumar',height/2  + 16,(255-alph,255-alph,255-alph))
        sleep(.012)
    sleep(.5)
    pygame.mixer.music.stop()
    

def display_gif(folder): # for best results we need gifs of app. same size
    n=0
    count = 2 # for no of times the gif to display
	#ready sequence
    static_display('Ready...',height/2,orange)
    sleep(1)
    gameDisplay.fill(white)
    static_display('Rock.',height/2,orange)
    sleep(.8)# this is causing freeze up
    gameDisplay.fill(white)
    static_display('Paper..',height/2,orange)
    sleep(.8)
    gameDisplay.fill(white)
    gameDisplay.fill(white)
    static_display('Scissors...',height/2,orange)
    sleep(.8)
    gameDisplay.fill(white)
    
    if folder =='rock':
        path = 'rock/'
        n = 20
        d1 = width * .3
        d2 = height * .35
        static_display('Rock',48,green)
    elif folder == 'paper':
        path = 'paper/'
        n = 21
        d1 = width * .29
        d2 = height * .2
        static_display('Paper',48, blue)
    elif folder == 'scissor':
        path = 'scissors/'
        n = 20
        d1 = width * .18
        d2 = height *.1
        static_display('Scissors',48,red)

    while(count > 0):
        for i in range (0,n):
            full_path = str(path +str(i)+str('.png'))
            paperimg = pygame.image.load(full_path)
            gameDisplay.blit(paperimg,(d1,d2))
            pygame.display.update()
            if (i < (n-1)):
                sleep(.07) # so that it doesnt sleeps in last one 
        count = count -1
                
#to display text with various content and color
def display_text(text,color,d1,d2):
    
    surface = gamefont.render(text,True,color)
    rect = surface.get_rect()
    rect.center = ((d1),(d2))
    gameDisplay.blit(surface,rect)
    pygame.display.update()
    sleep(refresh_rate)
    gameDisplay.fill(white)
    pygame.display.update()    

def static_display(text,display_height,color):
    
    surface = gamefont.render(text,True,color)
    rect = surface.get_rect()
    rect.center = ((width/2),(display_height))
    gameDisplay.blit(surface,rect)
    pygame.display.update()


#Game Logic.
def begin_game(): 
    control = random.randint(0,2)
    refresh_rate = .1 
    if (control == 0):
        display_gif('rock')
    elif (control == 1):
        display_gif('paper')
    elif (control == 2):
        display_gif('scissor')    

        
clock = pygame.time.Clock()
flag =0


crash = False
while not crash: #Event Loop
    #first iteration
    if flag==0:
        gameDisplay.fill(white)
        pygame.display.update()
        loading_Screen(0.2)
        flag+=1
        static_display('Press END button to Play.',width/2 + 18 , white)
        pygame.mixer.music.load('music/gameloop.mp3')
   
        #getting events 
    for event in pygame.event.get():
        
        if event.type == pygame.QUIT: #exiting sequence
            pygame.mixer.music.stop()
            gameDisplay.fill(white)
            pygame.display.update()
            exit_Screen()
            crash = True
            pygame.quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_END:
                if flag == 1 :
                     pygame.mixer.music.play(-1)
                     flag+=1
                gameDisplay.fill(white)
                pygame.display.update()
                begin_game()
                static_display('Press END button to play again',15,dark_green)
        elif event.type==VIDEORESIZE: # for resizing
            gameDisplay=pygame.display.set_mode(event.dict['size'],HWSURFACE|DOUBLEBUF|RESIZABLE) #resize 
    clock.tick(60)
pygame.quit()



