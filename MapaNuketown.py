import pygame
#uso de teclado y raton
from pygame.locals import * 
from pygame.constants import *  

# Cargamos las bibliotecas de OpenGL
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

# IMPORT OBJECT LOADER
from objloader import * #requerimos pasar esta parte al main

import math

# Se carga el archivo de la clase Cubo
import sys
sys.path.append('..')
from Casa import Casa
from Persona import Persona
from Vehiculo import Vehiculo
from Suelo import Suelo
from Letrero import Letrero 
from Valla import Valla
from Decoracion import Decoracion
from Lampara import Lampara
from Fondo import Fondo

screen_width = 900
screen_height = 600
#vc para el obser.
FOVY=60.0
ZNEAR=0.01
ZFAR=1000.0
# ZFAR=1000.0
#Variables para definir la posicion del observador
#gluLookAt(EYE_X,EYE_Y,EYE_Z,CENTER_X,CENTER_Y,CENTER_Z,UP_X,UP_Y,UP_Z)

# EYE_X = 1.0   #300.0
# EYE_Y = 7.0   #200.0
# EYE_Z = 0.0   #300.0
# CENTER_X = 0.0    #0
# CENTER_Y = 7.0    #0
# CENTER_Z = 0.0    #0
#pruebas dentro casa verde
EYE_X = 60.0   #300.0
EYE_Y = 7.0   #200.0
EYE_Z = 20.0   #300.0
CENTER_X = 0.0    #0
CENTER_Y = 7.0    #0
CENTER_Z = 0.0    #0
#pruebas
#EYE_X = 300.0
#EYE_Y = 200.0
#EYE_Z = 300.0
#CENTER_X = 0
#CENTER_Y = 0
#CENTER_Z = 0
#pruebas dentro cubo 2

# EYE_X = 90.0
# EYE_Y = 49.0
# EYE_Z = 90.0
# CENTER_X = 0
# CENTER_Y = 0
# CENTER_Z = 0

#pruebas dentro del cubo
# EYE_X = 300.0
# EYE_Y = 90.0
# EYE_Z = 300.0
# CENTER_X = 0
# CENTER_Y = 90
# CENTER_Z = 0
'''
#pruebas dentro del cubo casa amarilla
EYE_X = 1.0
EYE_Y = 50.0
EYE_Z = 0.0
CENTER_X = 0
CENTER_Y = 50
CENTER_Z = 0
'''
#pruebas centro del mapa
'''
EYE_X = 100.0
EYE_Y = 49.0
EYE_Z = 100.0
CENTER_X = 0
CENTER_Y = 0
CENTER_Z = 0
'''

UP_X=0
UP_Y=1
UP_Z=0
#Variables para dibujar los ejes del sistema
X_MIN=-500
X_MAX=500
Y_MIN=-500
Y_MAX=500
Z_MIN=-500
Z_MAX=500
#Dimension del plano
DimBoard = 400

#Variables para el control de las personas
personas = []
npersonas = 10

#Variables asociados las decoraciones de la casa
decoraciones = []
ndecoraciones = 13

#Variables para el control del observador
theta = 1.0
radius = 300
dir = [1.0, 0.0, 0.0]


pygame.init()

def Axis():
    glShadeModel(GL_FLAT)
    glLineWidth(3.0)
    #X axis in red
    glColor3f(1.0,0.0,0.0)
    glBegin(GL_LINES)
    glVertex3f(X_MIN,0.0,0.0)
    glVertex3f(X_MAX,0.0,0.0)
    glEnd()
    #Y axis in green
    glColor3f(0.0,1.0,0.0)
    glBegin(GL_LINES)
    glVertex3f(0.0,Y_MIN,0.0)
    glVertex3f(0.0,Y_MAX,0.0)
    glEnd()
    #Z axis in blue
    glColor3f(0.0,0.0,1.0)
    glBegin(GL_LINES)
    glVertex3f(0.0,0.0,Z_MIN)
    glVertex3f(0.0,0.0,Z_MAX)
    glEnd()
    glLineWidth(1.0)


def Init():
    #global obj
    global casa, casa2, bus, carro, suelo, suelo2, letrero, vallaC, vallaL1, vallaL2, vallaL3, vallaM1, vallaM2
    global alfombra, amongus, cama, closet, cocinaLavabo, foco, mesaySillas, muebleIndividual, muebleMediano
    global lampara, muebleMedianoParaTele, muebleParaTele, sillonGrande, sillonIndividual
    global fondo, fondo2, fondo3, fondo4, fondo5
    #screen = pygame.display.set_mode(
        #(screen_width, screen_height), DOUBLEBUF | OPENGL)
    screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN | pygame.DOUBLEBUF | pygame.OPENGL)
    pygame.display.set_caption("OpenGL: Mapa Nuketown")

    screen_info = pygame.display.Info()
    screen_width = screen_info.current_w
    screen_height = screen_info.current_h
    
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(FOVY, screen_width/screen_height, ZNEAR, ZFAR)

    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    gluLookAt(EYE_X,EYE_Y,EYE_Z,CENTER_X,CENTER_Y,CENTER_Z,UP_X,UP_Y,UP_Z)
    
    glClearColor(0,0,0,0)
    glEnable(GL_DEPTH_TEST)
    glPolygonMode(GL_FRONT_AND_BACK, GL_FILL)
    
    #Configuramos la iluminacion
    glLightfv(GL_LIGHT0, GL_POSITION,  (-40, 200, 100, 0.0))
    glLightfv(GL_LIGHT0, GL_AMBIENT, (0.2, 0.2, 0.2, 1.0))
    glLightfv(GL_LIGHT0, GL_DIFFUSE, (0.5, 0.5, 0.5, 1.0))
    glEnable(GL_LIGHT0)
    glEnable(GL_LIGHTING)
    glEnable(GL_COLOR_MATERIAL)
    glEnable(GL_DEPTH_TEST)
    glShadeModel(GL_SMOOTH)           # most obj files expect to be smooth-shaded
    
    
    # fondo = Fondo("Proyecto FInal\Fondo\FondoDesierto.obj")
    # fondo.generate()
    
    # Texturas para el suelo
    suelo = Suelo("Proyecto FInal\Texturas\BaseSuelo.obj")
    suelo.generate()
    suelo2 = Suelo("Proyecto FInal\Texturas\Suelo.obj")
    suelo2.generate()
    # Texturas para las vallas
    vallaC = Valla("Proyecto FInal\Texturas\VallaChica1.obj")
    vallaC.generate()
    vallaL1 = Valla("Proyecto FInal\Texturas\VallaChica1.obj")
    vallaL1.generate()
    vallaL2 = Valla("Proyecto FInal\Texturas\VallaLarga2.obj")
    vallaL2.generate()
    vallaL3 = Valla("Proyecto FInal\Texturas\VallaLarga3.obj")
    vallaL3.generate()
    vallaM1 = Valla("Proyecto FInal\Texturas\VallaMediana1.obj")
    vallaM1.generate()
    vallaM2 = Valla("Proyecto FInal\Texturas\VallaMediana2.obj")
    vallaM2.generate()
    
    # Arreglo de la direccion de las texturas de las personas
    obj_files = ["Proyecto FInal\Texturas\persona.obj"]
    # Casa verde y amarilla
    casa = Casa("Proyecto FInal\Texturas\CasaVerde.obj")
    casa.generate()
    casa2 = Casa("Proyecto FInal\Texturas\CasaAmarilla.obj")
    casa2.generate()
    # Creamos el bus
    bus = Vehiculo("Proyecto FInal\Texturas\BusAmarillo.obj")
    bus.generate()
    carro = Vehiculo("Proyecto FInal\Texturas\Chevrolet_Camaro_SS_Low.obj")
    # Creamos el letrero
    letrero = Letrero("Proyecto FInal\Texturas\Letrero.obj")
    letrero.generate()
    
    #asignamos las texturas a los faros
    lampara = Lampara("Proyecto FInal\Texturas\Faros.obj")
    lampara.generate()
    #asignamos las texturas a cada objeto dentro de la casa
    alfombra = Decoracion("Proyecto FInal\Texturas\Alfombra.obj")
    alfombra.generate()
    amongus = Decoracion("Proyecto FInal\Texturas\Amongus.obj")
    amongus.generate()
    cama = Decoracion("Proyecto FInal\Texturas\Cama.obj")
    cama.generate()
    closet = Decoracion("Proyecto FInal\Texturas\Closet.obj")
    closet.generate()
    cocinaLavabo = Decoracion("Proyecto FInal\Texturas\CocinaLavabo.obj")
    cocinaLavabo.generate()
    foco = Decoracion("Proyecto FInal\Texturas\\foco.obj")
    foco.generate()
    mesaySillas = Decoracion("Proyecto FInal\Texturas\MesaySillas.obj")
    mesaySillas.generate()
    muebleIndividual = Decoracion("Proyecto FInal\Texturas\MuebleIndividual.obj")
    muebleIndividual.generate()
    muebleMediano = Decoracion("Proyecto FInal\Texturas\MuebleMediano.obj")
    muebleMediano.generate()
    muebleMedianoParaTele = Decoracion("Proyecto FInal\Texturas\MuebleMedianoParaTele.obj")
    muebleMedianoParaTele.generate()
    muebleParaTele = Decoracion("Proyecto FInal\Texturas\MuebleMedianoParaTele.obj")
    muebleParaTele.generate()
    sillonGrande = Decoracion("Proyecto FInal\Texturas\SillonGrande.obj")
    sillonGrande.generate()
    sillonIndividual = Decoracion("Proyecto FInal\Texturas\SillonIndividual.obj")
    sillonIndividual.generate()
    
    # Texturas para el fondo
    fondo = Fondo(["Proyecto FInal\Fondo\FondoDesierto.bmp"])
    fondo2 = Fondo(["Proyecto FInal\Fondo\FondoDesierto.bmp"])
    fondo3 = Fondo(["Proyecto FInal\Fondo\FondoDesierto.bmp"])
    fondo4 = Fondo(["Proyecto FInal\Fondo\FondoDesierto.bmp"])
   #fondo5 = Fondo(["ProyectoFinal_MapaNuketown\Proyecto FInal\Fondo \NubesDesenfocadas2.bmp"])
    #Asigamos las texturas a cada persona
    for i in range(npersonas):
        obj_file = obj_files[i % len(obj_files)]
        persona = Persona(60, 1.0+i/4, obj_file)
        personas.append(persona)
        
        
    
def display():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    #glEnable(GL_LIGHTING)
    Axis()
    #Se dibuja el plano verde
    #glColor3f(0.3, 1.0, 0.3)
    #gris
    glColor3f(0.3, 0.3, 0.3)
    glBegin(GL_QUADS)
    glVertex3d(-DimBoard, 0, -DimBoard)
    glVertex3d(-DimBoard, 0, DimBoard)
    glVertex3d(DimBoard, 0, DimBoard)
    glVertex3d(DimBoard, 0, -DimBoard)
    glEnd()
    #se dibuja el fondo
    #drawFondo()
    
    #glColor3f(1.0, 1.0, 1.0) 
    
    
    #se dibuja el suelo
    glBindTexture(GL_TEXTURE_2D, 0) 
    glPushMatrix()
    glScale(8,8,8)
    glTranslate(1.5, 0, 0)
    glRotate(69, 0, 1, 0)
    glRotate(90, 1, 0, 0)
  
    suelo.draw()
    glPopMatrix()
    
    #se dibuja el suelo2
   
    glPushMatrix()
    glScale(8,8,8)
    glTranslate(0, 0.08, 0)
    # glRotate(75, 0, 1, 0) #cambio para ver orientacion del suelo
    glRotate(105, 0, 1, 0)
    glRotate(-90, 1, 0, 0)
    #glRotate(90, 1, 0, 0) #cambio para ver orientacion del suelo
   
    suelo2.draw()
    glPopMatrix()
    
    #se dibujan las lamparas
    
    glPushMatrix()
    glScale(8,8,8)
    glTranslate(6.3, 0.1, 3.8)
    lampara.draw()
    glPopMatrix()
    
    #lampara 2
   
    glPushMatrix()
    glScale(8,8,8)
    glTranslate(5.8, 0.1, -7)
    lampara.draw()
    glPopMatrix()
    
    #lampara 3
    glPushMatrix()
    glScale(8,8,8)
    glTranslate(-5, 0.1, -8)
    lampara.draw()
    glPopMatrix()
    
    #lampara 4
    glPushMatrix()
    glScale(8,8,8)
    glTranslate(-3.5, 0.1, 6)
    lampara.draw()
    glPopMatrix()
    
    #se dibujan la casa verde
    glPushMatrix()
    glScale(7,7,7)
    glTranslate(20, 0, 6.3)
    glRotate(-18, 0, 1, 0)
    # glRotate(-90, 1, 0, 0 )
    # glRotate(-90, 0, 0, 1)
    casa.draw()
    #obj.render()
    glPopMatrix()
    
    #se dibuja la casa amarilla
    glPushMatrix()
    glScale(7,7,8)
    glTranslate(-18, 0, 3.5)
    glRotate(18, 0, 1, 0)
    #glTranslate(-30, 0, -10)
    # glRotate(-90, 1, 0, 0)
    # glRotate(-90, 0, 0, 1)
    casa2.draw()
    #obj.render()
    glPopMatrix()
    
    #se dibujan la casa verde2
    glPushMatrix()
    #glScalef(3.5, 3.5, 3.5)
    #glTranslate(30, 0, 10)
    glScale(7,7,7)
    glTranslate(0, 0, 30)
    glRotate(-90, 0, 1, 0)
    # glRotate(-90, 1, 0, 0 )
    # glRotate(-90, 0, 0, 1)
    casa.draw()
    #obj.render()
    glPopMatrix()
    
    
    #Dibuja las personas
    glPushMatrix()
    glScale(0.3,0.3,0.3)
    #glTranslate(120.0, 0.0, 0.0)
    #glTranslate(0, -3, 0)
    glTranslate(-6, -3, 25)
    #glRotate(-90, 1, 0, 0)
    for obj in personas:
        obj.draw()
        obj.update()
    glPopMatrix()
    
   
    #Se dibuja el bus
    glPushMatrix()
    glScale(5,5,5)
    glTranslate(4, 1.4, -5)
    # glRotate(-90, 1, 0, 0)
    bus.draw()
    glPopMatrix()
    
    #Se dibuja el bus2
    glPushMatrix()
    glScale(5,5,5)
    glTranslate(-8, 1.4, 2)
    #glRotate(-90, 1, 0, 0)
    bus.draw()
    glPopMatrix()
    
    #se dibuja el carro
    glPushMatrix()
    glScale(3,3,3)
    glTranslate(3, 1.4,-30)
    glRotate(90, 0, 1, 0)
    #glRotate(-90, 1, 0, 0)
    carro.draw()
    glPopMatrix()
    
    #se dibuja el carro casa verde
    glPushMatrix()
    glScale(3,3,3)
    glTranslate(27, 1.4, 26)
    glRotate(70, 0, 1, 0)
    #glRotate(-90, 1, 0, 0)
    carro.draw()
    glPopMatrix()
    
    #Se dibuja el letrero
    glPushMatrix()
    glScale(1,1,1)
    glTranslate(80, 1.4, -20)
    glRotate(-90, 0, 1, 0)
    glRotate(-90, 1, 0, 0)
    letrero.draw()
    glPopMatrix()
    
    #Se dibujan las vallas
    glPushMatrix()
    glScale(14,14,14)
    #glTranslate(12, 0, -5.5)
    glTranslate(6.5, 0, -4.8)
    glRotate(-21, 0, 1, 0)
    glRotate(-90, 1, 0, 0)
    vallaC.draw()
    glPopMatrix()
    
    glPushMatrix()
    glScale(7, 14, 7)
    #glTranslate(12, 0, -5.5)
    glTranslate(15.8, 0, -10)
    glRotate(65, 0, 1, 0)
    glRotate(-90, 1, 0, 0)
    vallaC.draw()
    glPopMatrix()
    
    #valla larga
    glPushMatrix()
    glScale(14, 14, 14)
    #glTranslate(12, 0, -5.5)
    glTranslate(13.8, 0.5, -4.6)
    glRotate(-18, 0, 1, 0)
    glRotate(-90, 1, 0, 0)
    vallaM1.draw()
    glPopMatrix()
    
    # se dibuja la decoracion de la casa
    glPushMatrix()
    glScale(6,6,6)
    glTranslate(25.8,0.1,10.5)
    glRotate(-15, 0, 1, 0)
    glRotate(-90, 1, 0, 0)
    alfombra.draw()
    glPopMatrix()
    
    #listo
    glPushMatrix()
    glTranslate(174.5,5.08,58.5)
    glScale(0.3,0.3,0.3)
    glRotate(100, 0, 1, 0)
    glRotate(-90, 1, 0, 0)
    amongus.draw()
    glPopMatrix()
    
    #listo
    glPushMatrix()
    glTranslate(174.2, 3.8, 61)
    glScale(0.3,0.3,0.3)
    glRotate(15, 0, 1, 0)
    glRotate(-90, 1, 0, 0)
    amongus.draw()
    glPopMatrix()
    
    #listo
    glPushMatrix()
    glTranslate(174.2, 2.7, 58.5)
    glScale(0.3,0.3,0.3)
    glRotate(45, 0, 1, 0)
    glRotate(90, 0, 0, 1)
    amongus.draw()
    glPopMatrix()
    
    #listo
    glPushMatrix()
    glScale(4,4,4)
    glTranslate(27,0.1,0.5)
    glRotate(160, 0, 1, 0)
    glRotate(-90, 1, 0, 0)
    cama.draw()
    glPopMatrix()
    
    #listo
    glPushMatrix()
    glScale(4,4,4)
    glTranslate(29,0.1,0.01)
    glRotate(-107, 0, 1, 0)
    glRotate(-90, 1, 0, 0)
    closet.draw()
    glPopMatrix()
    
    #listo
    glPushMatrix()
    glScale(5,5,5)
    glTranslate(19.5,0.1,9.1)
    glRotate(-20, 0, 1, 0)
    glRotate(-90, 1, 0, 0)
    cocinaLavabo.draw()
    glPopMatrix()
    
    #listo
    glPushMatrix()
    glScale(5,5,5)
    glTranslate(21,0.1,9)
    glRotate(75, 0, 1, 0)
    glRotate(-90, 1, 0, 0)
    mesaySillas.draw()
    glPopMatrix()
    
    #listo
    glPushMatrix()
    glTranslate(135,20,30)
    glScale(0.8,0.8,0.8)
    glRotate(90, 1, 0, 0)
    foco.draw()
    glPopMatrix()
    
    
    #listo
    glPushMatrix()
    glScale(3,3,3)
    glTranslate(55,0.1,17.8)
    glRotate(-90, 1, 0, 0)
    muebleIndividual.draw()
    glPopMatrix()
    
    #listo
    glPushMatrix()
    glScale(3,3,3)
    glTranslate(49.8,0.1,16.5)
    glRotate(-90, 1, 0, 0)
    muebleIndividual.draw()
    glPopMatrix()
    
    #listo
    glPushMatrix()
    glScale(3,3,3)
    glTranslate(49,0.1,19)
    glRotate(-90, 1, 0, 0)
    muebleIndividual.draw()
    glPopMatrix()
    
    #listo
    glPushMatrix()
    glScale(3,3,3)
    glTranslate(48.6,0.1,20.5)
    glRotate(-90, 1, 0, 0)
    muebleIndividual.draw()
    glPopMatrix()
    
    #listo
    glPushMatrix()
    glScale(3,3,3)
    glTranslate(48.1,0.1,22)
    glRotate(-90, 1, 0, 0)
    muebleIndividual.draw()
    glPopMatrix()
    
    #listo
    glPushMatrix()
    glScale(2,2,2)
    glTranslate(87.2,0.5,30)
    glRotate(-107, 0, 1, 0)
    glRotate(-90, 1, 0, 0)
    muebleMediano.draw()
    glPopMatrix()
    
    #listo
    glPushMatrix()
    glScale(2,2,2)
    glTranslate(87.2, 1.8, 30)
    glRotate(-107, 0, 1, 0)
    glRotate(-90, 1, 0, 0)
    muebleMediano.draw()
    glPopMatrix()
    
    
    #listo
    glPushMatrix()
    glTranslate(154,0.5,63)
    glScale(0.2,0.2,0.2)
    glRotate(75, 0, 1, 0)
    glRotate(-90, 1, 0, 0)
    muebleMedianoParaTele.draw()
    glPopMatrix()
    
    #listo
    glPushMatrix()
    glScale(6,6,6)
    glTranslate(28.5,0.1,11.2)
    glRotate(75, 0, 1, 0)
    glRotate(-90, 1, 0, 0)
    muebleParaTele.draw()
    glPopMatrix()
    
    #listo
    glPushMatrix()
    glScale(4,4,4)
    glTranslate(35,0,14.8)
    glRotate(-105, 0, 1, 0)
    glRotate(-90, 1, 0, 0)
    sillonGrande.draw()
    glPopMatrix()
    
    #listo
    glPushMatrix()
    glScale(4,4,4)
    glTranslate(40,0,13)
    glRotate(166, 0, 1, 0)
    glRotate(-90, 1, 0, 0)
    sillonIndividual.draw()
    glPopMatrix()
    
    #listo
    glPushMatrix()
    glScale(4,4,4)
    glTranslate(38.5,0,12.6)
    glRotate(166, 0, 1, 0)
    glRotate(-90, 1, 0, 0)
    sillonIndividual.draw()
    glPopMatrix()
    
    glColor3f(1.0, 1.0, 1.0) 
    
    glPushMatrix()
    glTranslate(0, 0,-100)
    fondo.drawFondo()
    glPopMatrix()
    
    glPushMatrix()
    glTranslate(0, 0, -550)
    fondo2.drawFondo()
    glPopMatrix()
    
    glPushMatrix()
    glRotate(90, 0, 1, 0)
    fondo3.drawFondo()
    glPopMatrix()
    
    glPushMatrix()
    glRotate(-90, 0, 1, 0)
    fondo4.drawFondo()
    glPopMatrix()
    
    #glPushMatrix()
    #glScale(1.5, 1.5, 1.5)
    #glTranslate(0, 100, 300)
    #glRotate(-90, 1, 0, 0)
    #fondo5.drawFondo()
    #glPopMatrix()
    
    pygame.display.flip()
    #pygame.time.wait(100)
    
done = False
Init()

# Mouse CAM
last_mouse_pos = pygame.mouse.get_pos()
sensitivity = 0.1
phi = 0  # Define phi con un valor inicial

center_x = screen_width // 2
center_y = screen_height // 2
pygame.mouse.set_pos((center_x, center_y))

mouse_intentional = False

pygame.mouse.set_visible(False)

while not done:
    for event in pygame.event.get():
        if event.type == pygame.MOUSEMOTION:
            # Obtener la posición actual del mouse
            current_pos = pygame.mouse.get_pos()

            # Si el mouse se ha movido desde el centro de la ventana intencionalmente
            if current_pos != (center_x, center_y):
                mouse_intentional = True
                delta_x = current_pos[0] - center_x
                delta_y = current_pos[1] - center_y

                theta += delta_x * sensitivity
                phi -= delta_y * sensitivity

                phi = max(min(phi, 89), -89)
                theta %= 360
                pygame.mouse.set_pos((center_x, center_y))
            else:
                mouse_intentional = False  # El movimiento del mouse fue debido a centrado, no intencional

        if not mouse_intentional:
            dir[0] = math.cos(math.radians(theta)) * math.cos(math.radians(phi))
            dir[1] = math.sin(math.radians(phi))
            dir[2] = math.sin(math.radians(theta)) * math.cos(math.radians(phi))

            CENTER_X = EYE_X + dir[0]
            CENTER_Y = EYE_Y + dir[1]
            CENTER_Z = EYE_Z + dir[2]

            glLoadIdentity()
            gluLookAt(EYE_X, EYE_Y, EYE_Z, CENTER_X, CENTER_Y, CENTER_Z, UP_X, UP_Y, UP_Z)

        if event.type == pygame.QUIT:
            done = True
        
        keys = pygame.key.get_pressed()
        
        #se controla el movimiento para adelante
        if keys[K_UP] or keys[K_w]:
            nueva_pos_x = EYE_X + dir[0]
            nueva_pos_z = EYE_Z + dir[2]
            if -380 <= nueva_pos_x <= 380 and -150 <= nueva_pos_z <= 300:
                EYE_X = nueva_pos_x
                EYE_Z = nueva_pos_z
                CENTER_X = CENTER_X + dir[0]
                CENTER_Z = CENTER_Z + dir[2]
                glLoadIdentity()
                gluLookAt(EYE_X, EYE_Y, EYE_Z, CENTER_X, CENTER_Y, CENTER_Z, UP_X, UP_Y, UP_Z)
        #se controla el movimiento para atras
        if keys[K_DOWN] or keys[K_s]:
            nueva_pos_x = EYE_X - dir[0]
            nueva_pos_z = EYE_Z - dir[2]
            if -380 <= nueva_pos_x <= 380 and -150 <= nueva_pos_z <= 300:
                EYE_X = nueva_pos_x
                EYE_Z = nueva_pos_z
                CENTER_X = CENTER_X + dir[0]
                CENTER_Z = CENTER_Z + dir[2]
                glLoadIdentity()
                gluLookAt(EYE_X, EYE_Y, EYE_Z, CENTER_X, CENTER_Y, CENTER_Z, UP_X, UP_Y, UP_Z)
        
        if keys[K_RIGHT] or keys[K_d]:
            # Movimiento hacia la derecha
            right = [-dir[2], 0, dir[0]]
            EYE_X += right[0]
            EYE_Z += right[2]
            CENTER_X += right[0]
            CENTER_Z += right[2]
            glLoadIdentity()
            gluLookAt(EYE_X, EYE_Y, EYE_Z, CENTER_X, CENTER_Y, CENTER_Z, UP_X, UP_Y, UP_Z)
        #se controla el movimieto de camara a la izquierda
        
        if keys[K_LEFT] or keys[K_a]:
            # Movimiento hacia la izquierda
            left = [dir[2], 0, -dir[0]]
            EYE_X += left[0]
            EYE_Z += left[2]
            CENTER_X += left[0]
            CENTER_Z += left[2]
            glLoadIdentity()
            gluLookAt(EYE_X, EYE_Y, EYE_Z, CENTER_X, CENTER_Y, CENTER_Z, UP_X, UP_Y, UP_Z)

        if keys[K_ESCAPE]:
            done = True
    # Generar las parejas de obj
    parejas_persona = Persona.parejasPersonas(personas)

    # Llamar a la función colisionDetection con las parejas
    Persona.colisionDetection(parejas_persona) 
    display()

pygame.quit()