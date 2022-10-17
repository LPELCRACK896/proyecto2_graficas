from gl import Raytracer, V3
from lpmath import matriz
from texture import *
from figures import *
from lights import *


width = 500
height = 500
centrox = 0
centroy = -1
centroz = 0
# Materiales

""" 





stone = Material(diffuse = (0.4, 0.4, 0.4), spec = 8)

earth = Material(texture=Texture('earthDay.bmp'), spec=64, matType=OPAQUE)
extra = Material(texture=Texture("casita.bmp"), spec=64, matType=OPAQUE)
"""

rgbDecmimal = lambda rgb: [a/256 for a in rgb]

floorWood = Material(diffuse=rgbDecmimal((107, 60, 30)), spec=8)
blueLeftWall = Material(diffuse=rgbDecmimal((76, 112, 138)), spec=8)
blueTopWall = Material(diffuse=rgbDecmimal((60, 78, 90)), spec=8)
redCloth = Material(texture=Texture('tela_roja.bmp'), diffuse = (0.8, 0.3, 0.3))
mirror = Material(diffuse = (0.9, 0.9, 0.9), spec = 64, matType = REFLECTIVE)
brick = Material(diffuse = (0.8, 0.3, 0.3), spec = 16)
pillow = Material()
yellowMirror = Material(diffuse = (0.9, 0.9, 0.2), spec = 64, matType = REFLECTIVE) 
material_opaco1 = Material(diffuse = (0.0546, 0.472, 0.0664), spec=32, matType=OPAQUE)
material_opaco2 = Material(diffuse = (0.994, 0.186, 0.233), spec=32, matType=OPAQUE)
brownMat = Material(diffuse=rgbDecmimal((56, 39, 31)))
glass = Material(diffuse = (0.9, 0.9, 0.9), spec = 64, ior = 1.5, matType = TRANSPARENT)
material_reflectivo1 = Material(diffuse = (0.384, 0.501, 0.605), spec=32, matType=REFLECTIVE)
material_reflectivo2 =Material(diffuse = (0.9, 0.9, 0.9), spec = 64, matType = REFLECTIVE)
blueMirror = Material(diffuse = (0.2, 0.2, 0.9), spec = 64, matType = REFLECTIVE)

material_transparente1 = Material(diffuse = (0.805, 0.513, 0.303), spec=32, matType=TRANSPARENT)
material_transparente2 = Material(diffuse = (0.804, 0.707, 0.973), spec=32,ior=2 ,matType=TRANSPARENT)
rtx = Raytracer(width, height)

rtx.envMap = Texture("casita.bmp")

rtx.lights.append( AmbientLight(intensity = 0.8 ))
rtx.lights.append( PointLight(point = (0,0,0) ))

""" rtx.lights.append( PointLight(point = (1,1,-1), constant=4))
rtx.lights.append( PointLight(point = (0.8,1,-1), constant=4))
rtx.lights.append( PointLight(point = (0.6,1,-1), constant=4))
rtx.lights.append( PointLight(point = (0.4,1,-1), constant=4))
rtx.lights.append( PointLight(point = (0.2,1,-1), constant=4))
rtx.lights.append( PointLight(point = (0,1,-1), constant=4))
rtx.lights.append( PointLight(point = (-0.2,1,-1), constant=4))
rtx.lights.append( PointLight(point = (-0.4,1,-1), constant=4))
rtx.lights.append( PointLight(point = (-0.6,1,-1), constant=4))
rtx.lights.append( PointLight(point = (-0.8,1,-1), constant=4)) """

posicionSuelo = (0, -10, -1)
posicionParedIzquierda = (-10, 1, 0)
posicionParedDerecha = (10, 1, 0)
posicionParedFondo = (0, 0, -40)

rtx.scene.append( Plane(position=posicionSuelo, normal=(0, 0.8, 0), material=floorWood )) # Piso de madera
rtx.scene.append( Plane(position=posicionParedIzquierda, normal=(0.8, 0, 0.02), material=blueLeftWall )) # Pared izquierda
rtx.scene.append( Plane(position=posicionParedFondo, normal=(0, 0, 1), material=blueTopWall))
rtx.scene.append( Plane(position=posicionParedDerecha, normal=(-0.8, 0, 0.02), material=blueLeftWall )) # Pared izquierda

bedSize = (.3, .4, .4)
rtx.scene.append( AABB(position=(0.4,-.8,-2.8), size = (.8, .2, 2), material = redCloth ))
rtx.scene.append( AABB(position=(0.35,-.6,-2.8), size = (.6, .05, .6), material = pillow ))
rtx.scene.append( Sphere(center=V3(0,.5,-1), radius = 0.1,material=yellowMirror ))
rtx.scene.append( AABB(position=(0,0,-10), size = (1, 1, 1), material = mirror ))

#rtx.scene.append( Cuadrilatero(position=(0,0,-1), size = (2, 2), material=floorWood) )

rtx.scene.append( AABB(position=(-0.6,-.8,-2.0), size = (.4, .6, 1), material = brownMat ))

rtx.scene.append( Sphere(center=V3(-0.55,-0.45,-2.4), radius = 0.05, material = material_reflectivo1))
rtx.scene.append( Sphere(center=V3(-0.55,-0.45,-2.2), radius = 0.05, material = material_reflectivo2))
rtx.scene.append( Sphere(center=V3(-0.55,-0.45,-2.0), radius = 0.05, material = material_transparente1))
rtx.scene.append( Sphere(center=V3(-0.55,-0.45,-1.8), radius = 0.05, material = material_transparente2))
rtx.scene.append( Sphere(center=V3(-0.55,-0.45,-1.6), radius = 0.05, material = glass))
rtx.scene.append( Sphere(center=V3(-0.55,-0.45,-1.4), radius = 0.05, material = blueMirror))

rtx.scene.append( AABB(position=(-0.6,-1,-6.0), size = (.4, 1.2, .4), material = brownMat ))

rtx.glRender()

rtx.glFinish("output.bmp")