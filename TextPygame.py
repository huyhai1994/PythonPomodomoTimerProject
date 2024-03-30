import pygame
class TextPygame:
    def __init__(self,OnGraphicWindow,Text,FontSize,Location):
        self.OnGraphicWindow = OnGraphicWindow
        self.Text = Text
        self.FontSize = FontSize
        self.Location = Location
        self.drawTextOnScreen ()
    def drawTextOnScreen(self):
        font = pygame.font.Font(None,self.FontSize)
        self.OnGraphicWindow.blit (font.render( self.Text  ,True,'white'),\
                                self.Location)
        
