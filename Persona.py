import pygame
from pygame.locals import *

# Cargamos las bibliotecas de OpenGL
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
# IMPORT OBJECT LOADER
from objloader import *

import random
import math

class Persona:
    def __init__(self, dim, vel,obj_file,swapyz=True):
        self.obj = OBJ(obj_file, swapyz)
        
        self.DimBoard = dim
        #Se inicializa una posicion aleatoria en el tablero
        self.Position = []
        self.Position.append(random.randint(-1 * self.DimBoard, self.DimBoard))
        self.Position.append(5.0)
        self.Position.append(random.randint(-1 * self.DimBoard, self.DimBoard))
        #Se inicializa un vector de direccion aleatorio
        self.Direction = []
        self.Direction.append(random.random())
        self.Direction.append(5.0)
        self.Direction.append(random.random())
        #Se normaliza el vector de direccion
        m = math.sqrt(self.Direction[0]*self.Direction[0] + self.Direction[2]*self.Direction[2])
        self.Direction[0] /= m
        self.Direction[2] /= m
        #Se cambia la maginitud del vector direccion
        self.Direction[0] *= vel
        self.Direction[2] *= vel
        
    
    def update(self):
        new_x = self.Position[0] + self.Direction[0]
        new_z = self.Position[2] + self.Direction[2]
        
        if(abs(new_x) <= self.DimBoard):
            self.Position[0] = new_x
        else:
            self.Direction[0] *= -1.0
            self.Position[0] += self.Direction[0]
        
        if(abs(new_z) <= self.DimBoard):
            self.Position[2] = new_z
        else:
            self.Direction[2] *= -1.0
            self.Position[2] += self.Direction[2]
            
    def parejasPersonas(personas):
        parejas = []
        for i in range(len(personas)):
            for j in range(i + 1, len(personas)):
                parejas.append((personas[i], personas[j]))
        return parejas

    def colisionDetection(parejas):
        for persona1, persona2 in parejas:
            # Nuestros cubos son de tamaño 5, por lo que nuestros radios serian de 2.5
            radio_persona1 = 5  
            radio_persona2 = 5

            # Calcular la posición futura de los cubos
            posicion_futura_persona1 = [persona1.Position[0] + persona1.Direction[0], persona1.Position[2] + persona1.Direction[2]]
            posicion_futura_persona2 = [persona2.Position[0] + persona2.Direction[0], persona2.Position[2] + persona2.Direction[2]]

            # Calcular la distancia entre los centros en posición futura
            distancia = math.sqrt((posicion_futura_persona1[0] - posicion_futura_persona2[0]) ** 2 + (posicion_futura_persona1[1] - posicion_futura_persona2[1]) ** 2)

            # Verificar colisión
            if distancia <= (radio_persona1 + radio_persona2):
                # Dejamos quietos a los cubos
                #persona1.Direction = [0.0, persona1.Direction[1], 0.0]
                #persona2.Direction = [0.0, persona2.Direction[1], 0.0]
                #Los cubos rebotan en direcciones opuestas cuando colisionan
                persona1.Direction = [-1 * persona1.Direction[0], persona1.Direction[1], -1 * persona1.Direction[2]]
                persona2.Direction = [-1 * persona2.Direction[0], persona2.Direction[1], -1 * persona2.Direction[2]]
        
    def generate(self):
        self.obj.generate()

    def draw(self):
        glDisable(GL_TEXTURE_2D)
        glPushMatrix()
        glTranslatef(self.Position[0], self.Position[1], self.Position[2])
        glRotate(-90, 1, 0, 0)
        glScale(3.5,3.5,3.5)
        #glScale(0.8,0.8,0.8)
        #glScale(3,3,3)
        self.obj.render()
        glPopMatrix()
        
    