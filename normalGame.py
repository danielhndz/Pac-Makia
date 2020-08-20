from objects import *
import pygame, sys
from pygame.locals import *
from tkinter import messagebox

def move(windowG, current, nextt , board, pacman, cookies, lghost):
        board[current[0]][current[1]] = 'x'
        board[nextt[0]][nextt[1]] = 'pacman'
        imagefondo = pygame.image.load('Images/fondogame.jpg')
        if current[1] != nextt[1]:
            if current[1] < nextt[1]:
                for i in range(30):
                    pacman.image =  pygame.image.load("Images/pacman2.png")
                    windowG.blit(imagefondo,(0,0))
                    pacman.rect.left += pacman.velocidad
                    y1 =50
                    Fuente = pygame.font.Font(None,25)
                    labelscore = Fuente.render("SCORE: "+str(pacman.score),0,(255,255,255))
                    windowG.blit(labelscore,(10,10))
                    labelives = Fuente.render("LIVES: "+str(pacman.vidas),0,(255,255,255))
                    windowG.blit(labelives,(200,10))
                    for i in board:
                        x1 = 100
                        for j in i:
                            if j == 1:
                                obs = obstacle(x1,y1,"Images/obs.png")
                                obs.dibujar(windowG)
                            x1+=30
                        y1+=30
                    for i in cookies:
                        if i.rect.colliderect(pacman.rect):
                            cookies.remove(i)
                            pacman.score+=10
                        else:
                            i.dibujar(windowG)
                    pacman.dibujar(windowG)
                    for i in lghost:
                        i.dibujar(windowG)
                    pygame.display.update()
            else:
                for i in range(30):
                    if i%1 == 0:
                        pacman.image =  pygame.image.load("Images/pacman_left.png")
                    else:
                        pacman.image =  pygame.image.load("Images/pacman1.png")
                    windowG.blit(imagefondo,(0,0))
                    pacman.rect.left -= pacman.velocidad
                    y1 = 50
                    Fuente = pygame.font.Font(None,25)
                    labelscore = Fuente.render("SCORE: "+str(pacman.score),0,(255,255,255))
                    windowG.blit(labelscore,(10,10))
                    labelives = Fuente.render("LIVES: "+str(pacman.vidas),0,(255,255,255))
                    windowG.blit(labelives,(200,10))
                    for i in board:
                        x1 = 100
                        for j in i:
                            if j == 1:
                                obs = obstacle(x1,y1,"Images/obs.png")
                                obs.dibujar(windowG)
                            x1+=30
                        y1+=30
                    for i in cookies:
                        if i.rect.colliderect(pacman.rect):
                            cookies.remove(i)
                            pacman.score+=10
                        else:
                            i.dibujar(windowG)
                    pacman.dibujar(windowG)
                    for i in lghost:
                        i.dibujar(windowG)
                    pygame.display.update()
                    
        elif current[0] != nextt[0]:
            if current[0] < nextt[0]:
                for i in range(30):
                    pacman.image =  pygame.image.load("Images/pacman_down.png")
                    windowG.blit(imagefondo,(0,0))
                    pacman.rect.top += pacman.velocidad
                    y1 =50
                    Fuente = pygame.font.Font(None,25)
                    labelscore = Fuente.render("SCORE: "+str(pacman.score),0,(255,255,255))
                    labelives = Fuente.render("LIVES: "+str(pacman.vidas),0,(255,255,255))
                    windowG.blit(labelives,(200,10))
                    windowG.blit(labelscore,(10,10))
                    for i in board:
                        x1 = 100
                        for j in i:
                            if j == 1:
                                obs = obstacle(x1,y1,"Images/obs.png")
                                obs.dibujar(windowG)
                            x1+=30
                        y1+=30
                    for i in cookies:
                        if i.rect.colliderect(pacman.rect):
                            pacman.score+=10
                            cookies.remove(i)
                        else:
                            i.dibujar(windowG)
                    pacman.dibujar(windowG)
                    for i in lghost:
                        i.dibujar(windowG)
                    pygame.display.update()
            else:
                for i in range(30):
                    pacman.image =  pygame.image.load("Images/pacman_up.png")
                    windowG.blit(imagefondo,(0,0))
                    pacman.rect.top -= pacman.velocidad
                    y1 =50
                    Fuente = pygame.font.Font(None,25)
                    labelscore = Fuente.render("SCORE: "+str(pacman.score),0,(255,255,255))
                    windowG.blit(labelscore,(10,10))
                    labelives = Fuente.render("LIVES: "+str(pacman.vidas),0,(255,255,255))
                    windowG.blit(labelives,(200,10))
                    for i in board:
                        x1 = 100
                        for j in i:
                            if j == 1:
                                obs = obstacle(x1,y1,"Images/obs.png")
                                obs.dibujar(windowG)
                            x1+=30
                        y1+=30
                    for i in cookies:
                        if i.rect.colliderect(pacman.rect):
                            cookies.remove(i)
                            pacman.score+=10
                        else:
                            i.dibujar(windowG)
                    pacman.dibujar(windowG)
                    for i in lghost:
                        i.dibujar(windowG)
                    pygame.display.update()
            
            

def normalgame(board):
    pygame.init()
    imagefondo = pygame.image.load('Images/fondogame.jpg')
    x1 = 200 + 30*len(board[0])
    y1 = 80 + 30*len(board)
    windowG = pygame.display.set_mode((x1,y1))
    pygame.display.set_caption('pacman')
    y1 = 50
    fant = ["Images/green_center.png","Images/red_center.png","Images/pink_center.png","Images/yellow_center.png"]
    band = 0
    cf = 0
    cookies = []
    lghost = []
    for i in board:
        x1 = 100
        for j in i:
            if j == 'pacman':
                pacman = player(x1,y1,"Images/pacman2.png")
                pacman.dibujar(windowG)
            elif j == 1:
                obs = obstacle(x1,y1,"Images/obs.png")
                obs.dibujar(windowG)
            elif j == 'f':
                if cf >= len(fant):
                    cf=0
                ghost = enemy(x1,y1,fant[cf])
                lghost.append(ghost)
                cf+=1
            else:
                cook = cookie(x1,y1,"Images/cookie.png")
                cook.dibujar(windowG)
                cookies.append(cook)
            x1+=30
        y1+=30
    if len(cookies) > 0:
        pygame.display.update()
    pacman.score = 0
    while True:
        if pacman.vidas == 0:
                messagebox.showinfo("Game over", "YOU LOST THE GAME  :(")
                break
        y1 = 50
        fant = ["Images/green_center.png","Images/red_center.png","Images/pink_center.png","Images/yellow_center.png"]
        band = 0
        windowG.blit(imagefondo,(0,0))
        Fuente = pygame.font.Font(None,25)
        labelscore = Fuente.render("SCORE: "+str(pacman.score),0,(255,255,255))
        windowG.blit(labelscore,(10,10))
        labelives = Fuente.render("LIVES: "+str(pacman.vidas),0,(255,255,255))
        windowG.blit(labelives,(200,10))
        for i in board:
            x1 = 100
            for j in i:
                if j == 'pacman':
                    pacman.dibujar(windowG)
                elif j == 1:
                    obs = obstacle(x1,y1,"Images/obs.png")
                    obs.dibujar(windowG)
                x1+=30
            y1+=30
        for i in lghost:
            i.dibujar(windowG)
        for i in cookies:
            i.dibujar(windowG)
        if len(cookies) == 0:
            messagebox.showinfo("Game over", "¡¡YOU WON THE GAME!!")
            sys.exit()
            break
        for evento in pygame.event.get():
            if evento.type == QUIT:        
                pygame.quit()
                sys.exit()
            if evento.type == pygame.KEYDOWN:
                for i in range (len(board)):
                    for j in range(len(board[0])):
                        if board[i][j] == 'pacman':
                            start = (i,j)
                            break
                if evento.key == K_LEFT:
                    nextt = (start[0],start[1]-1)
                elif evento.key == K_RIGHT:
                    nextt = (start[0],start[1]+1)
                elif evento.key == K_UP:
                    nextt = (start[0]-1,start[1])
                elif evento.key == K_DOWN:
                    nextt = (start[0]+1,start[1])
                if  nextt[0] < len(board) and nextt[0] >= 0 and nextt[1] < len(board[0]) and nextt[1] >= 0 and board[nextt[0]][nextt[1]] == 'f':
                    move(windowG, start, nextt, board, pacman, cookies, lghost)
                    pacman.image = pygame.image.load("Images/pacman_dead.png")
                    pacman.dibujar(windowG)
                    board[nextt[0]][nextt[1]] = 'f'
                    board[-1][0] = 'pacman'
                    pacman.image = pygame.image.load("Images/pacman2.png")
                    pacman.rect.left = 100
                    pacman.rect.top = 20 + 30*len(board)
                    pacman.vidas -= 1
                elif nextt[0] < len(board) and nextt[0] >= 0 and nextt[1] < len(board[0]) and nextt[1] >= 0 and board[nextt[0]][nextt[1]] != 1:
                    move(windowG, start, nextt, board, pacman, cookies, lghost)
                    pygame.display.update()
        pygame.display.update()
    pygame.quit()
    sys.exit()   
