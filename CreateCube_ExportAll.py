import bpy
from random import randint

bpy.ops.mesh.primitive_cube_add()
path_to_export = "/Users/ryancosean/Desktop/Shooter/Model"

# how many cubes you want to add
count = 10

for c in range(0, count):
    x = randint(-10, 10)
    y = randint(-10, 10)
    z = randint(-10, 10)
    bpy.ops.mesh.primitive_cube_add(location=(x, y, z))

# export every object in-scene into fbx
bpy.ops.object.select_all(action='DESELECT')
sce = bpy.data.collections['Collection']
for ob in sce.objects:
    bpy.ops.object.select_pattern(pattern=ob.name)
    bpy.ops.bake_space_transform
    bpy.ops.export_scene.fbx(filepath=path_to_export + "/" + ob.name + ".fbx", use_selection=True,bake_space_transform=True)
    bpy.ops.object.select_all(action='TOGGLE')





