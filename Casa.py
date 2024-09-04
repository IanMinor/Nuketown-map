import pygame
from pygame.locals import *

# Cargamos las bibliotecas de OpenGL
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
# IMPORT OBJECT LOADER
from objloader import *


class Casa:
    def __init__(self, obj_file, swapyz=True):
        self.obj = OBJ(obj_file, swapyz)
        self.position = [0.0, 0.0, 0.0]  # La posición de la Casa
        self.size = [10.0, 10.0, 10.0]  # El tamaño de la Casa

    def generate(self):
        self.obj.generate()

    def draw(self):
        glPushMatrix()
        glRotate(-90, 1, 0, 0 )
        glRotate(-90, 0, 0, 1)
        self.obj.render()
        glPopMatrix()

    def check_collision(self, eye_position):
        min_x, min_y, min_z = [self.position[i] - self.size[i] / 2 for i in range(3)]
        max_x, max_y, max_z = [self.position[i] + self.size[i] / 2 for i in range(3)]

        eye_x, eye_y, eye_z = eye_position

        if min_x < eye_x < max_x and min_y < eye_y < max_y and min_z < eye_z < max_z:
            return True  # Hay colisión
        else:
            return False  # No hay colisión