class SumRecordDeepTime:
    def __init__(self,TimePass):
        self.TimePass = TimePass
        self.TotalTimePass = 0
    def SumTime(self):
        self.TotalTimePass +=  self.TimePass
        return  self.TotalTimePass
