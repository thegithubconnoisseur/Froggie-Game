import pygame
from object import *

class Frog(Object):
    def __init__(self, position, size, image, group, collision_groups, river_speeds):
        super().__init__(position, size, image, group)
        
        self.keyups = []

        self.collision_groups = collision_groups # all of the groups the frog can collide with

        self.river_speeds = river_speeds
        self.x_speed = 0 # used for when moving on a log or turtle

    def moveFrog(self):
        x = self.position[0]
        y = self.position[1]
        if pygame.K_UP in self.keyups or self.joystick_button_up:
            # Handle joystick UP event
            self.image_directory = "assets/frog/frog_up.png"
            y -= 48

        if pygame.K_DOWN in self.keyups or self.joystick_button_down:
            # Handle joystick DOWN event
            self.image_directory = "assets/frog/frog_down.png"
            y += 48

        if pygame.K_LEFT in self.keyups or self.joystick_button_left:
            # Handle joystick LEFT event
            self.image_directory = "assets/frog/frog_left.png"
            x -= 48

        if pygame.K_RIGHT in self.keyups or self.joystick_button_right:
            # Handle joystick RIGHT event
            self.image_directory = "assets/frog/frog_right.png"
            x += 48
        



        # if "joy_keyLeft" in self.keyups:
        #     self.image_directory = "assets/frog/frog_left.png"
        #     x -=48
        # if "joy_keyRight" in self.keyups:
        #     self.image_directory = "assets/frog/frog_right.png"
        #     x +=48

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

    def handleJoystickEvent(self, event):
        if event.type == pygame.JOYBUTTONDOWN:
            if event.button == 0:
                self.joystick_button_up = True
            elif event.button == 1:
                self.joystick_button_down = True
            elif event.button == 2:
                self.joystick_button_left = True
            elif event.button == 3:
                self.joystick_button_right = True

        if event.type == pygame.JOYBUTTONUP:
            if event.button == 0:
                self.joystick_button_up = False
            elif event.button == 1:
                self.joystick_button_down = False
            elif event.button == 2:
                self.joystick_button_left = False
            elif event.button == 3:
                self.joystick_button_right = False

    def killFrog(self):
        self.x_speed = 0
        self.position = (336, 672) # set back to start position
        self.image_directory = "assets/frog/frog_up.png"
        self.setImage()

    def update(self):
        self.handleJoystickEvent(pygame.event.poll())
        self.setImage()
        self.moveFrog()
        self.checkCollisions()
