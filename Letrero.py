import pygame
from pygame.locals import *

# Cargamos las bibliotecas de OpenGL
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
# IMPORT OBJECT LOADER
from objloader import *

class Letrero:
    def __init__(self, obj_file, swapyz=True):
        self.obj = OBJ(obj_file, swapyz)

    def generate(self):
        self.obj.generate()

    def draw(self):
        self.obj.render()   