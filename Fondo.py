import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
from objloader import *

class Fondo:
    def __init__(self, texture_paths):
        self.textures = [self.load_texture(image_path) for image_path in texture_paths]
    
    def load_texture(self, image_path):
        # Load image
        image = pygame.image.load(image_path)
        image = pygame.transform.flip(image, False, True)
        image_data = pygame.image.tostring(image, "RGB", 1)
        
        # Generate a texture id
        texture_id = glGenTextures(1)

        # Bind the texture
        glBindTexture(GL_TEXTURE_2D, texture_id)

        # Set texture parameters
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR)
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR)

        # Upload texture
        glTexImage2D(GL_TEXTURE_2D, 0, GL_RGB, image.get_width(), image.get_height(), 0, GL_RGB, GL_UNSIGNED_BYTE, image_data)

        return texture_id

    def drawFondo(self):
        vertex_coords = [
            # Coordenadas de la pared que quieres texturizar
            1, 1, 1,  -1, 1, 1,  -1, -1, 1,  1, -1, 1
        ]
        element_array = [0, 1, 2, 3]

        texture_coords = [
            0, 0,  1, 0,  1, 1,  0, 1  # Coordenadas de textura para la pared frontal
        ]

        # Dibujamos la pared
        glPushMatrix()
        glScalef(400.0, 350.0, 400.0)
        glTranslatef(0.0, 0.9, 0.0)

        glEnable(GL_TEXTURE_2D)
        glEnableClientState(GL_VERTEX_ARRAY)
        glEnableClientState(GL_TEXTURE_COORD_ARRAY)

        glVertexPointer(3, GL_FLOAT, 0, vertex_coords)
        glTexCoordPointer(2, GL_FLOAT, 0, texture_coords)

        # Utilizamos glDrawElements para dibujar solo la pared
        glBindTexture(GL_TEXTURE_2D, self.textures[0]) 
        glDrawElements(GL_QUADS, len(element_array), GL_UNSIGNED_INT, element_array)

        glDisable(GL_TEXTURE_2D)
        glDisableClientState(GL_VERTEX_ARRAY)
        glDisableClientState(GL_TEXTURE_COORD_ARRAY)
        glPopMatrix()
