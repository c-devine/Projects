import bpy
import os
import math

class Xflr5Body:
	def __init__(self, number):
		self.number = number
		self.coordArray = []
	
def add_cross_sections(context, sections):
	for section in sections:
		coords = []
		edges = []
		i = 0
		cLength = len(section.coordArray)
		for coord in section.coordArray:
			coords.append(coord)
			if i == cLength - 1 :
				edges.append([i,0])
			else:
				edges.append([i, i+1])
			i += 1
		name = "section " + str(section.number)
		mesh = bpy.data.meshes.new(name)
		objName = "obj" + name
		obj = bpy.data.objects.new(objName, mesh)
		obj.location = (0.0, 0.0, 0.0)
		context.scene.objects.link(obj)
		mesh.from_pydata(coords, edges, [])
		mesh.update(calc_edges=False)  
		obj.select = False 
			
	return
		   

def import_body_file(context, filepath, use_some_setting):
	print("parsing file " , filepath)
	
	sections = []
	f = open(filepath, 'r', encoding='utf-8')
	for line in f:
		if (len(line) > 0):
			if "Cross Section" in line:  
				cs = Xflr5Body(int(line.split(",")[1]))
				while True:			
					xyz = f.readline().split(",")
					if len(xyz) == 3:
						coord = float(xyz[0]), float(xyz[1]), float(xyz[2])
						cs.coordArray.append(coord)
						#print("adding " + xyz[0] + " " + xyz[1] + " " + xyz[2])
					else:
						break
				sections.append(cs)
	print("found " + str(len(sections)) + " sections")
	f.close()
	add_cross_sections(context, sections)
	print("done")

	return {'FINISHED'}


# ImportHelper is a helper class, defines filename and
# invoke() function which calls the file selector.
from bpy_extras.io_utils import ImportHelper
from bpy.props import StringProperty, BoolProperty, EnumProperty
from bpy.types import Operator


class ImportXflr5Body(Operator, ImportHelper):
	"""XFLR5 Body Importer"""
	bl_idname = "import_xflr5_body.data"  # important since its how bpy.ops.import_test.some_data is constructed
	bl_label = "Import Body Data"

	# ImportHelper mixin class uses this
	filename_ext = ".txt"

	filter_glob = StringProperty(
			default="*.txt",
			options={'HIDDEN'},
			)

# List of operator properties, the attributes will be assigned
	# to the class instance from the operator settings before calling.
	use_setting = BoolProperty(
			name="Example Boolean",
			description="Example Tooltip",
			default=True,
			)

	type = EnumProperty(
			name="Example Enum",
			description="Choose between two items",
			items=(('OPT_A', "First Option", "Description one"),
				   ('OPT_B', "Second Option", "Description two")),
			default='OPT_A',
			)

	def execute(self, context):
		return import_body_file(context, self.filepath, self.use_setting)


# Only needed if you want to add into a dynamic menu
def menu_func_import(self, context):
	self.layout.operator(ImportXflr5Body.bl_idname, text="XFLR5 Body Import Operator")


def register():
	bpy.utils.register_class(ImportXflr5Body)
	bpy.types.INFO_MT_file_import.append(menu_func_import)


def unregister():
	bpy.utils.unregister_class(ImportXflr5Body)
	bpy.types.INFO_MT_file_import.remove(menu_func_import)


if __name__ == "__main__":
	register()

   

	# test call
	bpy.ops.import_xflr5_body.data('INVOKE_DEFAULT')