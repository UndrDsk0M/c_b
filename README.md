# C_B: custom_blender.py 

+ Do you work with blender? 
- that perfect tool for 3d modeling?
+ Yes exaclly! how should i learn writing python codes in that? 
+ the bpy python codes are to long and hard to remmember :(
- Dont be worry look what i have found! c_b!

 C_B, this cute face can make your job so much faster than past 
 and you can learn blender by python very easier even than graphic!!


do you still write like this? 
```python
bpy.ops.mesh.primitive_cube_add(size=3, location=(0,0,0)
```

why you dont try this:
```python
cube()
```

do you remove all objects in 3 lines? why?
do it in one line:
```python
remove('all')
```

### example image1 :
![image](https://github.com/user-attachments/assets/5da27ee4-3ffd-4386-b2d0-c937cfd7d2f4)

![image](https://github.com/user-attachments/assets/de67417d-9cdc-4ebf-b284-7ec23d3da7ff)

### example image2 :
![image](https://github.com/user-attachments/assets/7947a257-4c42-4724-b125-83ac0cb2ce8e)

![image](https://github.com/user-attachments/assets/36d53ea3-e043-47a1-ada4-d3c3d0ffe09a)


### how about documention? oh you can use python help, github help, and telegram channel t.me/EHSAN_VK 
```python
print(help(cube))

# this will be the output
"""

This function create [cube] 
| Inputs:
| |
| | name(str): the name that you want give to your object ( it can be none, blender will give it a name)
| | size(int): size of object. defualt=3 Tip: (it prefer to use scale if available)
| | pos(int, int, int): the location or position of the object
| | rotat(float, float, float): rotation (x dir, y dir, z dir)
| | scale(int, int, int): make bigger, smaller. changes the size

| | 
| |
| |Tip: in most cases both float and int are accept_____________________
|
| Outputs:
| |
| | type of the output is a dict, that include a blender object and type of object
| | these information can be usefull if you want to work with that later so keep them in a verible
| |______________________________________________________________________________________________
|                    
|                    
|  c_b (custom_blender.py :] ) 
|  press q to quit
|____________________|
    
"""
```

## if you dont know blender and just python, its very simple to undrstand the simple things and coding
you can use print(help(cube)) to see the every func doc

it will have a huge update with minimum size, be ready for it!

v-0.0.2 update aded:
+ better documenting
+ rotation & scale 

featurs :
+ adding object by one line
+ creating function return that object so you will not lose your time in select and find the object
+ simple and easy removing (all or just a verible or name of object)


more in the way ...
