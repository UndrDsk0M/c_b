import bpy


def document(func,
            type_func: str = "create",
            object_type: str = 'function_name',
            name: bool = True,
            size: bool = True,
            pos: bool = True,
            depth: bool = False,
            radius: bool = False,
            rotat: bool = True,
            scale: bool = True,
            defualt_out: bool = True,
            *args, **kwargs):
    """this function create a text document for each functions """
    object_type = func.__name__
    name:  str|None = "| | name(str): the name that you want give to your object ( it can be none, blender will give it a name)\n" if name else '' 
    size:  str|None = "| | size(int): size of object. defualt=3 Tip: (it prefer to use scale if available)\n" if size else ''
    depth: str|None = "| | depth(float): actully its height i dont know why they say depth (tip: in both pos (z+, z-) will grow)\n" if depth else ''
    radius:str|None = "| | radius(float) that line in the circlelly part (it make bigger or smaller)\n" if radius else ''
    pos:   str|None = "| | pos(int, int, int): the location or position of the object\n" if pos else ''
    rotat: str|None = "| | rotat(float, float, float): rotation (x dir, y dir, z dir)\n" if rotat else ''
    scale: str|None = "| | scale(int, int, int): make bigger, smaller. changes the size\n" if scale else ''
    other: str|None = "| | {}".format(kwargs['more'] if 'more' in kwargs else '')
    output_:str|None = """| | type of the output is a dict, that include a blender object and type of object
| | these information can be usefull if you want to work with that later so keep them in a verible""" if defualt_out else kwargs['output']
    
    doc = f"""
This function {type_func} [{object_type}] 
| Inputs:
| |
{name}{size}{depth}{radius}{pos}{rotat}{scale}
{other}
| |
| |Tip: in most cases both float and int are accept_____________________
|
| Outputs:
| |
{output_}
| |______________________________________________________________________________________________
|                    
|                    
|  c_b (custom_blender.py :] ) 
|  press q to quit
|____________________|
    """    
    if __name__ == "__main__":
        print(doc)

    
    func.__doc__ = doc




    

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


def cube(name: str = None, pos: tuple[int, int, int] = (0, 0, 0), rotat: tuple[float, float, float] = (0.0, 0.0, 0.0), scale: tuple[float, float, float] = (0.0, 0.0, 0.0), size: int = 3, ) -> dict:
    """Create a cube object and saving in a verible"""

    bpy.ops.mesh.primitive_cube_add(size=size, location=pos, rotation=rotat, scale=scale)
    object_ = bpy.context.active_object
    if name : 
        __naming__(name=name, object_=object_)
    return {"object": object_,
            "type": "object",}



def monkey(name: str = None, pos: tuple[int, int, int] = (0, 0, 0), rotat: tuple[float, float, float] = (0.0, 0.0, 0.0), scale: tuple[float, float, float] = (0.0, 0.0, 0.0), size: int = 3, ) -> dict:
    """Create a monkey_head(suzan) object and saving in a verible"""

    bpy.ops.mesh.primitive_monkey_add(size=size, location=pos, rotation=rotat, scale=scale)
    object_ = bpy.context.active_object
    if name : 
        __naming__(name=name, object_=object_)
    return {"object": object_,
            "type": "object",}


def plane(name: str = None, pos: tuple[int, int, int] = (0, 0, 0), rotat: tuple[float, float, float] = (0.0, 0.0, 0.0), scale: tuple[float, float, float] = (0.0, 0.0, 0.0), size: int = 3, ) -> dict:
    """Create a plane(square) object and saving in a verible"""

    bpy.ops.mesh.primitive_plane_add(size=size, location=pos, rotation=rotat, scale=scale)
    object_ = bpy.context.active_object
    if name : 
        __naming__(name=name, object_=object_)
    return {"object": object_,
            "type": "object",}

def circle(name: str = None, pos: tuple[int, int, int] = (0, 0, 0), radius: int|float=1, rotat: tuple[float, float, float] = (0.0, 0.0, 0.0), scale: tuple[float, float, float] = (0.0, 0.0, 0.0), size: int = 3, ) -> dict:
    """Create a circle(2d) object and saving in a verible"""

    bpy.ops.mesh.primitive_circle_add(size=size, location=pos, rotation=rotat, scale=scale, radius=radius)
    object_ = bpy.context.active_object
    if name : 
        __naming__(name=name, object_=object_)
    return {"object": object_,
            "type": "object",}

def sphere(name: str = None, pos: tuple[int, int, int] = (0, 0, 0), rotat: tuple[float, float, float] = (0.0, 0.0, 0.0), scale: tuple[float, float, float] = (0.0, 0.0, 0.0), radius: int = 1, style: str = "uv") -> dict:
    """Create a sphere(3D_circle) object and saving in a verible *Tip: have two style*"""
    if style == "ico":
        bpy.ops.mesh.primitive_ico_sphere_add(radius=radius, location=pos)
    else :
        bpy.ops.mesh.primitive_uv_sphere_add(radius=radius, location=pos, rotation=rotat, scale=scale)

    object_ = bpy.context.active_object
    if name : 
        __naming__(name=name, object_=object_)
    return {"object": object_,
            "type": "object",}

def cylinder(name: str = None, pos: tuple[int, int, int] = (0, 0, 0), rotat: tuple[float, float, float] = (0.0, 0.0, 0.0), scale: tuple[float, float, float] = (0.0, 0.0, 0.0), radius: int = 1, depth: int = 2) -> dict:
    """Create a cylinder object and saving in a verible"""
    bpy.ops.mesh.primitive_cylinder_add(radius=radius, depth=depth, location=pos, rotation=rotat, scale=scale)
    object_ = bpy.context.active_object
    if name : 
        __naming__(name=name, object_=object_)
    return {"object": object_,
            "type": "object",}

def cone(name: str = None, pos: tuple[int, int, int] = (0, 0, 0), rotat: tuple[float, float, float] = (0.0, 0.0, 0.0), scale: tuple[float, float, float] = (0.0, 0.0, 0.0), radius: int = 1, depth: int = 2) -> dict:
    """Create a cone object and saving in a verible *Tip: no size, but have radius and depth """
    bpy.ops.mesh.primitive_cone_add(radius1=radius,depth=depth, location=pos, rotation=rotat, scale=scale)
    object_ = bpy.context.active_object
    if name : 
        __naming__(name=name, object_=object_)
    return {"object": object_,
            "type": "object",}


def torus(name: str = None, pos: tuple[int, int, int] = (0, 0, 0), rotat: tuple[float, float, float] = (0.0, 0.0, 0.0), scale: tuple[float, float, float] = (0.0, 0.0, 0.0), size: int = 3, style: str = "uv") -> dict:
    """Create a torus(donut) object and saving in a verible"""
    bpy.ops.mesh.primitive_torus_add(align="WORLD", location=pos, rotation=rotat, scale=scale)
    object_ = bpy.context.active_object
    if name : 
        __naming__(name=name, object_=object_)
    return {"object": object_,
            "type": "object",}

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

document(cube)
document(monkey)
document(plane)
document(circle, radius=True)
document(sphere, radius=True, more="style('uv', 'ico'): you can choose style of sphere that you want")
document(cylinder, radius=True, depth=True, size=False)
document(cone, radius=True, depth=True, size=False)
document(torus)
document(remove, type_func= 'delete',object_type='selected_object', name=False, size=False, pos=False, rotat=False, scale=False, more='target(name or object varible or all) all parameter delete all objects in scene, you can select by returned varible or name',defualt_out=False, output="| | It have no output")
print(help(remove))


remove('all')
cube('cu', (0, 0, 0))
monkey('suz', (5, 0, 0))
sphere('sp', (10, 0, 0))
cone('cn', (15, 0, 0))
cylinder('cl', (20, 0, 0))


















