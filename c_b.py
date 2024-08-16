import bpy
from time import sleep
__creating_doc__ = """
This function({}) {} [{}] 
  | Inputs:
  | |
  | | name(str): the name that you want give to your object (can be none blender will naming it)
  | | size(int): the size of that object (defualt = 3)
  | | pos((int, int, int)): the location or position of the object you want to be
  | | {}
  | |____________________________________________________________________________
  |
  | Outputs:
  | |
  | | type of the output is a dict, that include a blender object and type of object
  | | these information can be usefull if you want to work with that later so keep them in a verible
  | |______________________________________________________________________________________________
  |                    
  |                    
  |  c_b (custom_blender.py :] ) 
  |____________________|
"""

__removing_doc__ = """
This function({}) {} [{}] 
  | Inputs:
  | |
  | | Targer(str|object): this argument get 3 format of data:
  | |  | 
  | |  | 1. all: this remove all shapes in scene
  | |  | 2. name: if you give the name of object
  | |  | 3. object: if you saved the cube() in a x verible, now you can do remove(x) Easiest one
  | |____________________________________________________________________________
  |                                    
  |  c_b (custom_blender.py :] ) 
  |____________________|
"""
def __naming__(name: str, object_):
    """Naming convention for objects in Blender"""
    if name == "all":
        raise NameError("all name is not allowed! ( you got this error becuase c_b use all name in remove func)")
    try : 
        bpy.data.objects[name]
        is_used = True
    except :
        is_used = False
    finally :
        if is_used :
            raise NameError("{name} object exist right now!, change the name. Tip: [Your object have been created right now but with other name and this will make controlling harder]")
        else :
            object_.name = name
def cube(name: str = None, pos: tuple[int, int, int] = (0, 0, 0), size: int = 3, ) -> dict:
    """Create a cube object and saving in a verible"""

    bpy.ops.mesh.primitive_cube_add(size=size, location=pos)
    object_ = bpy.context.active_object
    if name : 
        __naming__(name=name, object_=object_)
    return {"object": object_,
            "type": "object",}
cube.__doc__ = __creating_doc__.format('cube', 'create a', "cube", "")


def monkey(name: str = None, pos: tuple[int, int, int] = (0, 0, 0), size: int = 3, ) -> dict:
    """Create a monkey_head(suzan) object and saving in a verible"""

    bpy.ops.mesh.primitive_monkey_add(size=size, location=pos)
    object_ = bpy.context.active_object
    if name : 
        __naming__(name=name, object_=object_)
    return {"object": object_,
            "type": "object",}
monkey.__doc__ = __creating_doc__.format('monkey', 'create a', "monkey", "")

def plane(name: str = None, pos: tuple[int, int, int] = (0, 0, 0), size: int = 3, ) -> dict:
    """Create a plane(square) object and saving in a verible"""

    bpy.ops.mesh.primitive_plane_add(size=size, location=pos)
    object_ = bpy.context.active_object
    if name : 
        __naming__(name=name, object_=object_)
    return {"object": object_,
            "type": "object",}
plane.__doc__ = __creating_doc__.format('plane', 'create a', "plane", "")

def circle(name: str = None, pos: tuple[int, int, int] = (0, 0, 0), size: int = 3, ) -> dict:
    """Create a circle(2d) object and saving in a verible"""

    bpy.ops.mesh.primitive_circle_add(size=size, location=pos)
    object_ = bpy.context.active_object
    if name : 
        __naming__(name=name, object_=object_)
    return {"object": object_,
            "type": "object",}
circle.__doc__ = __creating_doc__.format('circle', 'create a', "circle", "")

def sphere(name: str = None, pos: tuple[int, int, int] = (0, 0, 0), size: int = 3, radius: int = 1, style: str = "uv") -> dict:
    """Create a sphere(3D_circle) object and saving in a verible *Tip: have two style*"""
    if style == "ico":
        bpy.ops.mesh.primitive_ico_sphere_add(radius=radius, location=pos)
    else :
        bpy.ops.mesh.primitive_uv_sphere_add(radius=radius, location=pos)

    object_ = bpy.context.active_object
    if name : 
        __naming__(name=name, object_=object_)
    return {"object": object_,
            "type": "object",}
sphere.__doc__ = __creating_doc__.format('sphere', 'create a', "sphere", "style(str): to parameters (uv, ico) defualt is uv")

def cylinder(name: str = None, pos: tuple[int, int, int] = (0, 0, 0), radius: int = 1, depth: int = 2) -> dict:
    """Create a cylinder object and saving in a verible"""
    bpy.ops.mesh.primitive_cylinder_add(radius=radius, depth=depth, location=pos)
    object_ = bpy.context.active_object
    if name : 
        __naming__(name=name, object_=object_)
    return {"object": object_,
            "type": "object",}
cylinder.__doc__ = __creating_doc__.format('cylinder', 'create a', "cylinder", "")


def cone(name: str = None, pos: tuple[int, int, int] = (0, 0, 0), radius: int = 1, depth: int = 2) -> dict:
    """Create a cone object and saving in a verible *Tip: no size, but have radius and depth """
    bpy.ops.mesh.primitive_cone_add(radius1=radius,depth=depth, location=pos)
    object_ = bpy.context.active_object
    if name : 
        __naming__(name=name, object_=object_)
    return {"object": object_,
            "type": "object",}
cone.__doc__ = __creating_doc__.format('cone', 'create a', "cone", "*Tip: You can not use size parameters in this object!*")


def torus(name: str = None, pos: tuple[int, int, int] = (0, 0, 0), size: int = 3, style: str = "uv") -> dict:
    """Create a torus(donut) object and saving in a verible"""
    bpy.ops.mesh.primitive_torus_add(align="WORLD", location=pos)
    object_ = bpy.context.active_object
    if name : 
        __naming__(name=name, object_=object_)
    return {"object": object_,
            "type": "object",}
torus.__doc__ = __creating_doc__.format('torus', 'create a', "torus", "")

def remove(target: object|str = "all"):
    """Remove object from scene *Tip: you should give a verible that created object or name of that (or just delete all as Defualt)"""
    if target == "all":
        bpy.ops.object.select_all(action='DESELECT')
        bpy.ops.object.select_by_type(type='MESH')
        bpy.ops.object.delete()
    elif type(target) == str:
        if target in bpy.data.objects:
            selected = bpy.data.objects[target]
            bpy.data.objects.remove(selected, do_unlink=True)
        else :
            raise NameError("the object that you choosed to delete is not exist: {target}".format())
    else :
        bpy.data.objects.remove(target['object'], do_unlink=True)
remove.__doc__ = __removing_doc__.format('remove', 'delete', "object you selected")