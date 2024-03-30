class RecordDeepTimePass:
    def __init__(self,TimePass):
        if TimePass == 0:
            self.TimePass = 1500
            self.recordTime = 0
        elif TimePass == 10:
            self.TimePass = 0
        else:
            self.TimePass =  10- TimePass
    def exportTimePass(self):
        return self.TimePass
