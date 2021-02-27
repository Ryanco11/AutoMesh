import cv2
import bpy
import random
import numpy as np
import bmesh

img = cv2.imread("/Users/ryancosean/Desktop/Cube.png", 0)
cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()

# remove all MESH objects
[bpy.data.objects.remove(obj) for obj in bpy.data.objects if obj.type == "MESH"]

# verts = []

for x in range(1, 10):
   for y in range(1, 10):
       for z in range(1, 10):
           bpy.ops.mesh.primitive_cube_add(location=(x, y, z))

