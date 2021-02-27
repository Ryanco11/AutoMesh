import bpy
import bmesh
import mathutils
from mathutils import Vector
from bpy.types import Operator
from bpy_extras.object_utils import AddObjectHelper, object_data_add
from bpy.props import FloatVectorProperty

verts = [(1, 1, 0), (-1, 1, 0)]

mesh = bpy.data.meshes.new("mesh")  # add a new mesh
obj = bpy.data.objects.new("MyObject", mesh)  # add a new object using the mesh

scene = bpy.context.scene
bpy.context.collection.objects.link(obj)  # put the object into the scene (link)
bpy.context.view_layer.objects.active = obj   # set as the active object in the scene
bpy.context.active_object.select_set(state=True)  # select object

mesh = bpy.context.object.data
bm = bmesh.new()

for v in verts:
    bm.verts.new(v)  # add a new vert

bm.edges.new(bm.verts)




# make the bmesh the object's mesh
bm.to_mesh(mesh)
bm.free()  # always do this when finished