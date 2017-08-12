# on dit a Python qu'on utilise Pygame
import pygame
pygame.init()

#
#############################################################################
# c'est le code qui definit ce que fera une PacBoule
# ca s'appelle une 'Classe'  
class Classe_des_PacBoules(pygame.sprite.Sprite):
    # __init__ est ce qui est fait quand on cree une PacBoule
    #   self, ca veut dire "moi-meme", ca sert a clairement identifier les informations
    #       d'une PacBoule par rapport aux autres informations du programme
    def __init__(self, Position_de_depart, Direction_de_depart, Vitesse_de_depart):
        pygame.sprite.Sprite.__init__(self)
        self.Position_actuelle = Position_de_depart
        self.Direction_actuelle = Direction_de_depart
        self.Vitesse_Actuelle = Vitesse_de_depart
        self.image = pygame.image.load('lecon01-images/PacVert.png').convert_alpha()
        self.rect = self.image.get_rect()
    #     
    #######################################################################
    # 'update' ca veut dire 'mise a jour' ...
    # c'est ce qui sera fait a chaque image, 50 fois par seconde dans notre cas
    def update(self, Nombre_de_milliseconde_depuis_le_dernier_appel):
        # si la PacBoule touche les bords verticaux
        # alors la direction horizontale change de sens 
        if self.Position_actuelle.x < 0 or self.Position_actuelle.x > Largeur_de_la_fenetre:
            self.Direction_actuelle.x = - self.Direction_actuelle.x 
        # meme verification avec les bords horizontaux
        if self.Position_actuelle.y < 0 or self.Position_actuelle.y > Hauteur_de_la_fenetre :
            self.Direction_actuelle.y  = - self.Direction_actuelle.y

        # on calcule le deplacement
        #   on multiple la vitesse par le temps ecoule
        #   et on multiple la direction par le tout
        #   cela nous donne de combien on se deplace    
        Deplacement = self.Direction_actuelle.normalize() * self.Vitesse_Actuelle * Nombre_de_milliseconde_depuis_le_dernier_appel
        
        # on rajoute le deplacement que l'on vient de calculer a notre position
        # et on a la nouvelle position de la PacBoule
        self.Position_actuelle = self.Position_actuelle + Deplacement

        # Pas grand chose a comprendre a cette ligne...
        #   'blit' ca veut dire 'mettre sur l'ecran'
        self.rect.x = self.Position_actuelle.x
        self.rect.y = self.Position_actuelle.y
        Fenetre.blit(self.image, self.rect)
    
#2
    def rebondir(self, axe):
        if axe == VERTICAL :
            self.Direction_actuelle.x = - self.Direction_actuelle.x 
        # meme verification avec les bords horizontaux
        elif axe == HORIZONTAL :
            self.Direction_actuelle.y  = - self.Direction_actuelle.y
    
    
        
        
##########################################################################
#

class Classe_des_Raquettes:
    def __init__(self, Position_de_depart, vitesse):
        pygame.sprite.Sprite.__init__(self)
        self.Position_actuelle = Position_de_depart
        self.Vitesse = vitesse

        self.image = pygame.Surface([10, 50])
        self.image.fill((255,255,255))
        self.rect = self.image.get_rect()
    
    def update(self, direction, Nombre_de_milliseconde_depuis_le_dernier_appel):
        if self.Position_actuelle.y < 0 :
            self.Position_actuelle.y = 0
        elif self.Position_actuelle.y > Hauteur_de_la_fenetre :
            self.Position_actuelle.y = Hauteur_de_la_fenetre
        else :
            deplacement = direction * Nombre_de_milliseconde_depuis_le_dernier_appel * self.Vitesse 
            self.Position_actuelle.y = self.Position_actuelle.y + deplacement
            self.rect.x = self.Position_actuelle.x
            self.rect.y = self.Position_actuelle.y
            Fenetre.blit(self.image, self.rect)
          
#
##########################################################################
# Dans cette section, il y a des informations generales sur le programme
#  
#le nombre de FPS, c-a-d d'image par seconde
Nombre_de_FPS = 50

# les informations sur la fenetre de jeu
#   la couleur du fond de la couleur, du noir car 0 de rouge, 0 de rouge, 0 de bleu
Couleur_du_fond_RVB = (0,0,0)

#   et la taille de la fenetre en pixels
Hauteur_de_la_fenetre = 300
Largeur_de_la_fenetre = 400
#   (x,y) c'est la facon dont Python stocke les coordonnees
Taille_de_la_fenetre = (Largeur_de_la_fenetre,Hauteur_de_la_fenetre)

####
HAUT = 1
BAS = -1

HORIZONTAL = 1
VERTICAL = -1

# c'est la facon dont PyGame creer une fenetre pour l'afficher sur l'ecran
Fenetre = pygame.display.set_mode(Taille_de_la_fenetre)

# 'caption', ca veut dire 'etiquette' en gros.
# 'set_caption', ca veut 'mettre dans l'etiquette
pygame.display.set_caption("une PacBoule")

# on a besoin d'un horloge pour compte le nombre d'image par seconde,
#   et faire les calculs avec la vitesse
#   Tous les programmes PyGame utilise cela 
Horloge = pygame.time.Clock()

# on compte toujours les millesecondes ecoulees, donnees par l'Horloge
Nombre_de_millisecondes_ecoulee = 0

# bah, la... il faut connaitre un peu les maths et les vecteurs...
#   ca se comprend assez bien avec un dessin
Position = pygame.math.Vector2(100,100)
Direction = pygame.math.Vector2(10,10)
# la vitesse est en nombre de pixel par milliseconde
Vitesse = .3

# on cree la PacBoule !
La_boule = Classe_des_PacBoules(Position,Direction,Vitesse)
#2
Groupe_de_la_boule = pygame.sprite.Group()
Groupe_de_la_boule.add(La_boule)
#2
Position = pygame.math.Vector2(50,50)
La_raquette = Classe_des_Raquettes(Position, Vitesse )

#2
Mouvement_de_la_souris = pygame.math.Vector2(0,0)

sortie_du_jeu = False 

##########################################################################
# c'est la boucle d'evenement, qui est infinie sauf si ...
# il y en a toujours une dans les programmes PyGame
while not sortie_du_jeu:
    # on attend un peu pour avoir le bon nombre de FPS
    # 'tick' attend AU MOINS un certain nombre de millisecondes
    # et retourne le nombre de millisecondes reellement ecoule 
    Nombre_de_millisecondes_ecoulee = Horloge.tick(Nombre_de_FPS)
    Nombre_de_millisecondes_ecoulee = 20

    # au fur et a mesure du jeu, il faut effacer l'ecran precedent
    # 'fill' veut dire 'remplir'
    # dans notre cas, on remplir d'une couleur uniforme
    Fenetre.fill(Couleur_du_fond_RVB)


    # rien a comprendre ici pour l'instant
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sortie_du_jeu = True
            
    Mouvement_de_la_souris = pygame.math.Vector2(pygame.mouse.get_rel())
    #Mouvement_de_la_souris = pygame.math.Vector2(1,1)
    if Mouvement_de_la_souris.y < 0 :
        La_raquette.update(BAS,Nombre_de_millisecondes_ecoulee)
    elif Mouvement_de_la_souris.y > 0 :
        La_raquette.update(HAUT,Nombre_de_millisecondes_ecoulee)
    else:
        La_raquette.update(0,Nombre_de_millisecondes_ecoulee)
    # A chaque image, on appelle la fonction 'update' de la PacBoule
    # c'est cette fonction qui gere le mouvement
    La_boule.update(Nombre_de_millisecondes_ecoulee)

    if pygame.sprite.spritecollide(La_raquette, Groupe_de_la_boule, False):
        La_boule.rebondir(VERTICAL)

    # rien a comprendre 
    # ca met a jour les choses a afficher a l'ecran
    #pygame.display.update([La_boule.rectangle, La_raquette.rectangle])
    pygame.display.flip()


pygame.quit()