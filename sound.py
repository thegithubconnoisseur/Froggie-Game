from time import sleep

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(17, GPIO.OUT)
pin17 = GPIO.PWM(17,100)
pin17.start(50)
        
def playSound(frequency):
    play = True
    while play:
        GPIO.output(17, GPIO.HIGH)
        pin17.changeFrequency(frequency)
        sleep(1)
        pin17.changeFrequency(frequency) 
        sleep(1)
        play = False