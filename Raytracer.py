from dis import dis
from gl import Raytracer, V3
from lpmath import matriz
from texture import *
from figures import *
from lights import *


width = 100
height = 100
centrox = 0
centroy = -1
centroz = 0
# Materiales

""" material_opaco1 = Material(diffuse = (0.0546, 0.472, 0.0664), spec=32, matType=OPAQUE)
material_opaco2 = Material(diffuse = (0.994, 0.186, 0.233), spec=32, matType=OPAQUE)

material_reflectivo1 = Material(diffuse = (0.384, 0.501, 0.605), spec=32, matType=REFLECTIVE)
material_reflectivo2 =Material(diffuse = (0.9, 0.9, 0.9), spec = 64, matType = REFLECTIVE)

material_transparente1 = Material(diffuse = (0.805, 0.513, 0.303), spec=32, matType=TRANSPARENT)
material_transparente2 = Material(diffuse = (0.804, 0.707, 0.973), spec=32,ior=2 ,matType=TRANSPARENT)


brick = Material(diffuse = (0.8, 0.3, 0.3), spec = 16)
stone = Material(diffuse = (0.4, 0.4, 0.4), spec = 8)

earth = Material(texture=Texture('earthDay.bmp'), spec=64, matType=OPAQUE)
mirror = Material(diffuse = (0.9, 0.9, 0.9), spec = 64, matType = REFLECTIVE)
glass = Material(diffuse = (0.9, 0.9, 0.9), spec = 64, ior = 1.5, matType = TRANSPARENT)
extra = Material(texture=Texture("casita.bmp"), spec=64, matType=OPAQUE)
blueMirror = Material(diffuse = (0.2, 0.2, 0.9), spec = 64, matType = REFLECTIVE)
yellowMirror = Material(diffuse = (0.9, 0.9, 0.2), spec = 64, matType = REFLECTIVE) """

rgbDecmimal = lambda rgb: [a/256 for a in rgb]

floorWood = Material(diffuse=rgbDecmimal((107, 60, 30)))
blueLeftWall = Material(diffuse=rgbDecmimal((76, 112, 138)))
blueTopWall = Material(diffuse=rgbDecmimal((60, 78, 90)))

rtx = Raytracer(width, height)

#rtx.envMap = Texture("casita.bmp")

rtx.lights.append( AmbientLight(intensity = 0.8 ))


rtx.lights.append( PointLight(point = (1,1,-1), constant=4))
rtx.lights.append( PointLight(point = (0.8,1,-1), constant=4))
rtx.lights.append( PointLight(point = (0.6,1,-1), constant=4))
rtx.lights.append( PointLight(point = (0.4,1,-1), constant=4))
rtx.lights.append( PointLight(point = (0.2,1,-1), constant=4))
rtx.lights.append( PointLight(point = (0,1,-1), constant=4))
rtx.lights.append( PointLight(point = (-0.2,1,-1), constant=4))
rtx.lights.append( PointLight(point = (-0.4,1,-1), constant=4))
rtx.lights.append( PointLight(point = (-0.6,1,-1), constant=4))
rtx.lights.append( PointLight(point = (-0.8,1,-1), constant=4))

rtx.scene.append( Plane(position=(0, -1, -1), normal=(0, 0.8, 0.2),material=floorWood )) # Piso de madera
rtx.scene.append( Plane(position=(-1, 1, 0), normal=(0.8, 0, 0.02), material=blueLeftWall )) # Pared izquierda
rtx.scene.append( Plane(position=(0, 0, -4), normal=(0, 0, 1), material=blueTopWall))
rtx.scene.append( Plane(position=(1.4, 1, 0), normal=(-0.8, 0, 0.02), material=blueLeftWall )) # Pared izquierda


rtx.glRender()

rtx.glFinish("output.bmp")