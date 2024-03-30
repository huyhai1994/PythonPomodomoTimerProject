class convertSecond_to_MinutesAndSeconds:
    def __init__(self,Seconds):
        self.Seconds = Seconds
    def ConvertTime(self):
        self.display_Seconds  = self.Seconds %60
        self.display_Minutes  = int ( self.Seconds /60) % 60
        return     self.display_Seconds , self.display_Minutes 
