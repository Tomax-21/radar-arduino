import pygame
from pygame.locals import *

import math
pygame.init()
# paramétrage de l'écran
largeur = 1200
hauteur = 700
vert=(0,255,0)


noir = (0, 0 ,0)
grisNoir = (20,20,20)
rouge = (255, 0 ,0)
ecran = pygame.display.set_mode((largeur,hauteur))
ecran.fill(grisNoir)
pygame.display.flip()
continuer = True

PI = 3.141592653
angle = PI/2
fps = pygame.time.Clock()
distance = 492





while continuer == True:
    for event in pygame.event.get():
        if event.type == QUIT or (event.type == KEYUP and event.key == K_ESCAPE):
            continuer = False # si on ferme la fenêtre ou si on appuie sur la touche é chappement




    pygame.draw.circle(ecran,vert,(largeur//2,hauteur),400,2)
    pygame.draw.circle(ecran,vert,(largeur//2,hauteur),300,2)
    pygame.draw.circle(ecran,vert,(largeur//2,hauteur),200,2)
    pygame.draw.circle(ecran,vert,(largeur//2,hauteur),100,2)


    pygame.draw.line(ecran,vert,(largeur//2,200),(largeur//2,hauteur),7)



    # (x, y), (x, y)
    # initial, final


    x = distance * math.sin(angle) + largeur//2
    y = distance * math.cos(angle) + hauteur-11

    pygame.draw.line(ecran, vert, (largeur//2, hauteur-11), (x, y), 4)






    pygame.draw.line(ecran,vert,(100,hauteur-10),(largeur-100,hauteur-10),7)
    pygame.draw.circle(ecran,vert,(largeur//2,hauteur),500,5)
    pygame.draw.line(ecran,grisNoir,(100,hauteur),(largeur-100,hauteur),20)









    pygame.display.flip() # valide les changements de l affichage


    pygame.draw.line(ecran, grisNoir, (largeur//2, hauteur-11), (x, y), 4)
    angle = angle + .01


    if angle >  1.5*PI:
        angle = PI/2


    fps.tick(15)






pygame.quit()