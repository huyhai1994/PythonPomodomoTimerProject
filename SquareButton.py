import pygame
class SquareButton:
    def __init__(self, TopLeftLocation_X, TopLeftLocation_Y, image, scale):
        self.width = image.get_width()
        self.height = image.get_height()
        self.image = pygame.transform.scale(image, (int(self.width  * scale), int(self.height * scale)))
        self.imageBorder = self.image.get_rect()
        self.imageBorder.topleft = (TopLeftLocation_X, TopLeftLocation_Y)
        self.LeftMouseButton  = 0
        self.RightMouseButton = 1
        self.MousePressed  = 1
        self.MouseReleased = 0
        self.clicked = False
    def drawButton(self, OnGraphicWindow):
        self.width = self.image.get_width()
        self.height = self.image.get_height()
        pygame.draw.rect(OnGraphicWindow,'black',(self.imageBorder.x, self.imageBorder.y,50,50))
        OnGraphicWindow.blit(self.image, (self.imageBorder.x, self.imageBorder.y))
    def checkClicked(self):
        action = False
        self.clicked = False
        UserMousePosition = pygame.mouse.get_pos()
        #check mouseover and clicked conditions
        if self.imageBorder.collidepoint(UserMousePosition):
            if pygame.mouse.get_pressed()[self.LeftMouseButton] ==  self.MousePressed and self.clicked == False:
                self.clicked = True
                action = True
        if pygame.mouse.get_pressed()[self.LeftMouseButton]     ==  self.MouseReleased:
            self.clicked = False
        return action
