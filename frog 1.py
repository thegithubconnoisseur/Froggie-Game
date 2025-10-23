import pygame
from object import *

# import RPi.GPIO as GPIO
from time import sleep


class Frog(Object):
    def __init__(self, position, size, image, group, collision_groups, river_speeds):
        super().__init__(position, size, image, group)
        pygame.joystick.init()
        self.keyups = []
        self.joysticks = []
        self.joysticks =  [pygame.joystick.Joystick(x) for x in range (pygame.joystick.get_count())]
        print(self.joysticks)
        self.collision_groups = collision_groups # all of the groups the frog can collide with

        self.river_speeds = river_speeds
        self.x_speed = 0 # used for when moving on a log or turtle

    def moveFrog(self):
        x = self.position[0]
        y = self.position[1]
        for key in self.joysticks:
            if key.get_button(0):
                self.image_directory = "assets/frog/frog_right.png"
                x += 20
                print("workign")
            # A button
            if key.get_button(1):
                self.image_directory = "assets/frog/frog_down.png"
                y += 20
                print("which button is it")
            # B button
            if key.get_button(2):
                self.image_directory = "assets/frog/frog_up.png"
                y -= 20
                print("which button is up")
            # # x button
            if key.get_button(3):
                self.image_directory = "assets/frog/frog_left.png"
                x -= 20
                print("this is left Y")
                
        if pygame.K_UP in self.keyups:
            self.image_directory = "assets/frog/frog_up.png"
            y -= 48
            

        if pygame.K_DOWN in self.keyups:
            self.image_directory = "assets/frog/frog_down.png"
            y += 48

        if pygame.K_LEFT in self.keyups:
            self.image_directory = "assets/frog/frog_left.png"
            x -= 48

        if pygame.K_RIGHT in self.keyups:
            self.image_directory = "assets/frog/frog_right.png"
            x += 48

        x += self.x_speed # if on a turtle or log, move with it
        if x <= -48 or x > 48*14 or y > 48*16:
            self.killFrog()
            return

        self.position = (x,y)
        

    def checkCollisions(self):
        self.setImage()

        collided = False
        for sprite_group in self.collision_groups:
            if pygame.sprite.spritecollideany(self, sprite_group):
                collided = True

        lane = self.position[1]//48 # which lane is the frog in
        if collided:
            if lane < 8: # if colliding with a sprite while in the river (on a log or turtle)
                self.x_speed = self.river_speeds[lane]
            else: # in street colliding with sprite
                self.killFrog()
        else: # if not colliding with another sprite
            self.x_speed = 0
            if lane < 8: # frog not colliding with anything but is in the river
                self.killFrog()


    def killFrog(self):
        self.x_speed = 0
        self.position = (336, 672) # set back to start position
        self.image_directory = "assets/frog/frog_up.png"
        self.setImage()

        leds = [6, 13, 19, 21]

        # GPIO.setmode(GPIO.BCM)
        # GPIO.setup(leds, GPIO.OUT)


        # for i in range(len(leds)):
        #     #light the current LED
        #     GPIO.output(leds[i], True)
        #     sleep(0.3)
        #     GPIO.output(leds[i], False)
        #     sleep(0.3)
            
            

        # GPIO.cleanup

    def update(self):
        self.setImage()
        self.moveFrog()
        self.checkCollisions()
