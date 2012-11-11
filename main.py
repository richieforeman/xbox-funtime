__author__ = 'Richie Foreman <richie.foreman@gmail.com>'

import pygame
import sys
class XBoxController(object):
    button_callbacks = []

    BUTTON_A = 11
    BUTTON_B = 12
    BUTTON_X = 13
    BUTTON_Y = 14

    BUTTON_DOWN = pygame.JOYBUTTONDOWN
    PLAYER_ONE = 0
    PLAYER_TWO = 1
    PLAYER_THREE = 2
    PLAYER_FOUR = 3
    joystick = None

    def __init__(self, joystick=0):
        self.joystick = joystick

    def addButtonCallback(self, button, type, callback):
        self.button_callbacks.append({"button": button, "type": type, "callback": callback})

    def handleButtonEvent(self, e):
        button = e.dict["button"]
        type = e.type
        for d in self.button_callbacks:
            if d["button"] == button and d["type"] == e.type:
                d["callback"]()

    def loop(self):
        pygame.joystick.init()

        try:
            j = pygame.joystick.Joystick(self.joystick) # create a joystick instance
            j.init() # init instance
        except pygame.error:
            print 'No XBox Controller Found.'

        while True:
            e = pygame.event.wait()
            if e.type is pygame.JOYBUTTONDOWN:
                self.handleButtonEvent(e)
            elif e.type is pygame.JOYBUTTONUP:
                self.handleButtonEvent(e)


def a_down():
    sound = pygame.mixer.Sound('frog.wav')
    sound.play()

def b_down():
    sound = pygame.mixer.Sound("dog.wav")
    sound.play()

def y_down():
    sound = pygame.mixer.Sound("cat.wav")
    sound.play()

def main():
    pygame.mixer.init()
    pygame.display.init()

    xbox = XBoxController(joystick=XBoxController.PLAYER_ONE)

    xbox.addButtonCallback(button=XBoxController.BUTTON_A,
                           type=XBoxController.BUTTON_DOWN,
                           callback=a_down)
    xbox.addButtonCallback(button=XBoxController.BUTTON_B,
                           type=XBoxController.BUTTON_DOWN,
                           callback=b_down)
    xbox.addButtonCallback(button=XBoxController.BUTTON_Y,
                           type=XBoxController.BUTTON_DOWN,
                           callback=y_down)
    xbox.addButtonCallback(button=XBoxController.BUTTON_X,
                           type=XBoxController.BUTTON_DOWN,
                           callback=lambda: sys.stdout.write(str("hello") + "\n"))
    xbox.run()

# allow use as a module or standalone script
if __name__ == "__main__":
    main()