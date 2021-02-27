import bpy

verts = [(0, 0, 0), (0, 5, 0), (5, 5, 0), (5, 0, 0), (0, 0, 5), (0, 5, 5), (5, 5,5), (5, 0, 5)]

faces = [(0, 1, 2, 3), (7, 6, 5, 4), (0, 4, 5, 1), (1,5,6,2), (2,6,7,3), (3,7,4,0)]

myMesh = bpy.data.meshes.new("TRI")
myObject = bpy.data.objects.new("TRI", myMesh)

myObject.location = bpy.context.scene.cursor_location
bpy.context.scene.objects.link(myObject)

myMesh.from_pydata(verts, [], faces)
myMesh.update(calc_edges = True)