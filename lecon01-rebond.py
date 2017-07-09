# on dit a Python qu'on utilise Pygame
import pygame

#le nombre de FPS, c-a-d d'image par seconde
Nombre_de_FPS = 50

#on compte toujours les millesecondes
Nombre_de_millisecondes_ecoulee = 0

#les informations sur la fenetre de jeu
Couleur_du_fond_RVB = (0,0,0)
Hauteur_de_la_fenetre = 300
Largeur_de_la_fenetre = 400

#############################################################################
class Classe_des_PacBoules(pygame.sprite.Sprite):
    def __init__(self, Position_de_depart, Direction_de_depart, Vitesse_de_depart):
        pygame.sprite.Sprite.__init__(self)
        self.Position_actuelle = Position_de_depart
        self.Direction_actuelle = Direction_de_depart
        self.Vitesse_Actuelle = Vitesse_de_depart
        self.image = pygame.image.load('lecon01-images/PacVert.png').convert_alpha()
        self.rectangle = self.image.get_rect()

    def update(self, Nombre_de_milliseconde_depuis_le_dernier_appel):
        if self.Position_actuelle.x < 0 or self.Position_actuelle.x > Largeur_de_la_fenetre:
            self.Direction_actuelle.x = - self.Direction_actuelle.x 
        
        if self.Position_actuelle.y < 0 or self.Position_actuelle.y > Hauteur_de_la_fenetre :
            self.Direction_actuelle.y  = - self.Direction_actuelle.y

        Deplacement = self.Direction_actuelle.normalize() * self.Vitesse_Actuelle 
        self.Position_actuelle = self.Position_actuelle + Deplacement

        Fenetre.blit(self.image, self.Position_actuelle)

                



##########################################################################
# 
pygame.init()

Taille_de_la_fenetre = (Largeur_de_la_fenetre,Hauteur_de_la_fenetre)
Fenetre = pygame.display.set_mode(Taille_de_la_fenetre)
pygame.display.set_caption(pygame.version.ver)

Horloge = pygame.time.Clock()

Position = pygame.math.Vector2(100,100)
Direction = pygame.math.Vector2(10,10)
Vitesse = 10

La_boule = Classe_des_PacBoules(Position,Direction,Vitesse)



##########################################################################
# c'est la boucle d'evenement, qui est infinie sauf si ...
while True: