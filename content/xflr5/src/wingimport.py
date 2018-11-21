import bpy
import os
import math

class Xflr5Foil:
    def __init__(self, dataString, basePath, fileName):
        self.dataString = dataString
        self.basePath = basePath
        self.fileName = fileName
        self.coordArray = []
        self.xOffset = 0.0
        self.yOffset = 0.0
        self.zOffset = 0.0
        self.chord = 0.0
        self.twist = 0.0
        
    def parse(self):
        # parse the dataString
        dArray = self.dataString.split()
        #y,chord,offset,dihedral,twist,foil
        self.xOffset = float(dArray[2])
        self.yOffset = float(dArray[0])
        self.zOffset = float(dArray[3])
        self.chord = float(dArray[1])
        self.twist = float(dArray[4])
        
        # parse the foil file coordinates
        foilFile = os.path.join(self.basePath , self.fileName)
        print("parsing " + foilFile)
        f = open(foilFile, 'r', encoding='utf-8')
        # skip the first line
        f.readline()
        for line in f:
               xy = line.split()
               if len(xy) == 2:
                   self.coordArray.append([float(xy[0]), float(xy[1])])
                   
        print("found " + str(len(self.coordArray)) + " pairs")        
        f.close()   
        return

def add_foils(context, foils, rotate = True):
    for foil in foils:
        print("foil chord = " + str(foil.chord))
        coords = []
        edges = []
        i = 0
        cLength = len(foil.coordArray)
        for coord in foil.coordArray:
            coords.append([coord[0] * foil.chord, 0, coord[1] * foil.chord])
            print("input = " + str(coord) + " chord = " + str(foil.chord))
            print("output = " + str(coords[i]) )
            if i == cLength - 1 :
                edges.append([i,0])
            else:
                edges.append([i, i+1])
            i += 1
    
        mesh = bpy.data.meshes.new(foil.fileName)
        objName = "obj" +foil.fileName
        obj = bpy.data.objects.new(objName, mesh)
        obj.location = (foil.xOffset, foil.yOffset, 0.0)
        context.scene.objects.link(obj)
        mesh.from_pydata(coords, edges, [])
        mesh.update(calc_edges=False)  
        obj.select = True
        if (rotate):
            bpy.ops.transform.rotate( value = ( math.radians(foil.twist) ), axis = (0,1,0) )
             
        obj.select = False        
    return
           

def import_xwimp_file(context, filepath, use_some_setting):
    print("parsing file " , filepath)
    basePath = os.path.dirname(filepath)

    foils = []
    f = open(filepath, 'r', encoding='utf-8')
    f.readline()
    for line in f:
        print("line = ", line)
        if (len(line) >0):
            fileName = line.split()[9].replace("/_/"," ")
            print("foil name = ", str(fileName))
            foil = Xflr5Foil(line, basePath, fileName + ".dat")
            foil.parse()
            foils.append(foil)
     
    f.close()
    #print("found ", len(foils), " foils")
    #print("len foils[0] " + str(len(foils[0].coordArray)))
    add_foils(context, foils, False)
    print("done")

    return {'FINISHED'}


# ImportHelper is a helper class, defines filename and
# invoke() function which calls the file selector.
from bpy_extras.io_utils import ImportHelper
from bpy.props import StringProperty, BoolProperty, EnumProperty
from bpy.types import Operator


class ImportXflr5(Operator, ImportHelper):
    """XFLR5 XWIMP Importer"""
    bl_idname = "import_xflr5.xwimp_data"  # important since its how bpy.ops.import_test.some_data is constructed
    bl_label = "Import Foil Data"

    # ImportHelper mixin class uses this
    filename_ext = ".xwimp"

    filter_glob = StringProperty(
            default="*.xwimp",
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
        return import_xwimp_file(context, self.filepath, self.use_setting)


# Only needed if you want to add into a dynamic menu
def menu_func_import(self, context):
    self.layout.operator(ImportXflr5.bl_idname, text="XFLR5 Import Operator")


def register():
    bpy.utils.register_class(ImportXflr5)
    bpy.types.INFO_MT_file_import.append(menu_func_import)


def unregister():
    bpy.utils.unregister_class(ImportXflr5)
    bpy.types.INFO_MT_file_import.remove(menu_func_import)


if __name__ == "__main__":
    register()

   

    # test call
    bpy.ops.import_xflr5.xwimp_data('INVOKE_DEFAULT')