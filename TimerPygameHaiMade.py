import pygame, sys
from pygame.locals import*
from SquareButton import SquareButton
from ConvertCurrentSecond_to_MinutesAndSeconds import convertSecond_to_MinutesAndSeconds
from TextPygame import TextPygame
from getCurrentRealTime import getCurrentRealTime
import datetime
from playsound import playsound

OnGraphicWindowWIDTH = 600
OnGraphicWindowHEIGHT = 400
#            R    G    B
GRAY     = (100, 100, 100)
TOMATO   = (255, 99,  71)
BLACK    = 'black'

BackGroundColor = TOMATO
StartButtonImage = pygame.image.load('StartButton.png')
PauseButtonImage = pygame.image.load('PauseButton.png')
RecordButtonImage = pygame.image.load('RecordButton.png')

PauseButton_TopLeftCornerPositionX  = 525
PauseButton_TopLeftCornerPositionY  = 150
StartButton_TopLeftCornerPositionX  = 525
StartButton_TopLeftCornerPositionY  = 213
RecordButton_TopLeftCornerPositionX = 525
RecordButton_TopLeftCornerPositionY = 88
ProgressBar_TopLeftCornerPositionX  = 20
ProgressBar_TopLeftCornerPositionY  = 331
ProgressBar_Length                  = 558
ProgressBar_Height                  = 40
ProgressPercentage_TopLeftCornerPositionX = ProgressBar_Length  /2
ProgressPercentage_TopLeftCornerPositionY = 340
ProgressPercentageLocation          = (ProgressPercentage_TopLeftCornerPositionX, ProgressPercentage_TopLeftCornerPositionY)
ClockDomain_TopLeftCornerPositionX  = 20
ClockDomain_TopLeftCornerPositionY  = 50
ClockDomainWidth                    = 480
ClockDomainHeight                   = 250
ClockTextLocation                   = ( 63  ,98  )
PodometerTextLocation               = ( 190, 50)
TimePassedLocation                  = (38, 310)
displayCurrentRealTimeLocation      = (60, 280)
PodometerText                       = 'POMODORO'


def main():
    pygame.init()
    OnGraphicWindow = pygame.display.set_mode( (OnGraphicWindowWIDTH,\
                                                   OnGraphicWindowHEIGHT))
    pygame.time.set_timer(pygame.USEREVENT, 1000)
    OnGraphicWindow.fill (BackGroundColor )
    time = 1000
    ScaleRatio = 1
    PauseButton = SquareButton(PauseButton_TopLeftCornerPositionX ,\
                                                       PauseButton_TopLeftCornerPositionY,\
                                                       PauseButtonImage,ScaleRatio)
    StartButton = SquareButton( StartButton_TopLeftCornerPositionX ,\
                                                        StartButton_TopLeftCornerPositionY,\
                                                        StartButtonImage,ScaleRatio)
    RecordButton  = SquareButton( RecordButton_TopLeftCornerPositionX ,\
                                                        RecordButton_TopLeftCornerPositionY,\
                                                         RecordButtonImage,ScaleRatio)
    PODOMETERTIME = 1500
    sumTimePassed = 0
    TargetTime = 15000
    CurrentRealTime = ' '
    while 1:
        run = True
        PodometerTime                       = PODOMETERTIME
        started = False
        while run:
            OnGraphicWindow.fill (BackGroundColor )
            PauseButton.drawButton  (OnGraphicWindow)
            StartButton.drawButton  (OnGraphicWindow)
            RecordButton.drawButton (OnGraphicWindow)
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if started  == False and StartButton.checkClicked ():
                        started = True
                    elif started == True and PauseButton.checkClicked():
                        started = False
                    elif RecordButton.checkClicked ():
                        TimePassed          = PODOMETERTIME - PodometerTime
                        PodometerTime       = PODOMETERTIME
                        started = False
                        run = False
                if event.type == pygame.USEREVENT and started:
                    PodometerTime-= 1
                if event.type ==QUIT:
                    pygame.quit()
                    sys.exit()
            if PodometerTime >= 0:
                Clock = convertSecond_to_MinutesAndSeconds(PodometerTime)
                display_seconds, display_minutes = Clock.ConvertTime()
                TextPygame (OnGraphicWindow,f"{display_minutes:02}:{display_seconds:02}",250,ClockTextLocation)
            elif PodometerTime < 0:
                playsound('Ram Bell Sound.wav')
                CurrentRealTime = datetime.datetime.now()
                CurrentRealTime.strftime("%m/%d/%Y, %H:%M:%S")
                TimePassed = PODOMETERTIME
                TextPygame (OnGraphicWindow,f"{display_minutes:02}:{display_seconds:02}",250,ClockTextLocation)
                
         
                run = False
            LengthofProgresBar =    sumTimePassed /  TargetTime *ProgressBar_Length
            pygame.draw.rect(OnGraphicWindow,BLACK,(ProgressBar_TopLeftCornerPositionX,\
                                                   ProgressBar_TopLeftCornerPositionY,ProgressBar_Length,ProgressBar_Height))
            pygame.draw.rect(OnGraphicWindow,GRAY,(ProgressBar_TopLeftCornerPositionX,\
                                                  ProgressBar_TopLeftCornerPositionY,LengthofProgresBar,ProgressBar_Height))
            TextPygame (OnGraphicWindow, PodometerText, 50, PodometerTextLocation)
            TextPygame (OnGraphicWindow, str(  int(  sumTimePassed /  TargetTime *100))+'%', 30, ProgressPercentageLocation)
            getCurrentRealTime(CurrentRealTime, OnGraphicWindow, 50, displayCurrentRealTimeLocation)
            pygame.display.update()
        sumTimePassed +=  TimePassed
if __name__ =='__main__': main()

