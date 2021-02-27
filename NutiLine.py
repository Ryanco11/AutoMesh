import bpy
import bmesh
import mathutils
from mathutils import Vector
from bpy.types import Operator
from bpy_extras.object_utils import AddObjectHelper, object_data_add
from bpy.props import FloatVectorProperty
from mathutils import Matrix
from math import asin, pi, degrees, radians


angle = 10
mesh = bpy.data.meshes.new("mesh")  # add a new mesh
obj = bpy.data.objects.new("MyObject", mesh)  # add a new object using the mesh

scene = bpy.context.scene
bpy.context.collection.objects.link(obj)  # put the object into the scene (link)
bpy.context.view_layer.objects.active = obj   # set as the active object in the scene
bpy.context.active_object.select_set(state=True)  # select object

mesh = bpy.context.object.data
bm = bmesh.new()
test = []

V3 = bm.verts.new((1, 3, 0))
V2 = bm.verts.new((2, 0, 0))
V1 = bm.verts.new((-1, 0, 0))

bm.edges.new((V1, V2))
bm.edges.new((V2, V3))

#bmesh.ops.rotate(
#    bm, verts=bm.verts, matrix=Matrix.Rotation(pi * angle / 180, 3, 'Z'))

bm.to_mesh(mesh)
bm.free()  # always do this when finished