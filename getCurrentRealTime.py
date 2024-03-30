from TextPygame import TextPygame
import datetime

class getCurrentRealTime:
    def __init__(self, CurrentRealtime, OnGraphicWindow, FontSize, displayCurrentRealTimeLocation):
        self.CurrentRealtime     = CurrentRealtime
        self.OnGraphicWindow = OnGraphicWindow
        self.FontSize        = FontSize
        self.displayCurrentRealTimeLocation = displayCurrentRealTimeLocation
        self.displayOnGraphicWindow()
    def displayOnGraphicWindow (self):
        TextPygame(self.OnGraphicWindow, str( self.CurrentRealtime ), \
                   self.FontSize, self.displayCurrentRealTimeLocation)


