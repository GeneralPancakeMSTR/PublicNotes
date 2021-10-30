import bpy 
import os 
import re 
import glob 
import json

# Quick script for making changes to external file paths. 
# Currently only does image textures. 
# "write_paths=True" will find all the images in this blend file, 
# and write their name and path to "filepaths.txt" in the same directory as this blend file.
# "read_paths=True" will read from a similar file, also in this directory,
#  and for every name in this file, 
# will check for a corresponding image, 
# check if its path in the blend file is different from that read in,
# and update it if so. It reloads the image as well, to effect the change. 
# Note that the "filepaths" files are dictionaries of the form paths = <target name> : <absolute path>
# E.g. paths = <image name> : <absolute path>. 

os.system('cls')

here = os.path.dirname(bpy.data.filepath)

write_paths = False 
savelocation = os.path.join(here,'filepaths.txt')
if(write_paths):
    paths = {}
    with open(savelocation,'w+') as file:
        for image in bpy.data.images:
            if(image.filepath_from_user()):
                paths.update({image.name:image.filepath_from_user()})
                print(f'{image.name}    {image.filepath_from_user()}')
        json.dump(paths,file,indent=1)
    file.close()
        

read_paths = False
readlocation = os.path.join(here,'filepaths_new.txt')
#readlocation = os.path.join(here,'filepaths.txt')
if(read_paths):  
    with open(readlocation,'r') as file:
        paths = json.load(file)
    file.close()
    
    for name in paths:
        if(bpy.data.images[name]):
            image = bpy.data.images[name]
            if(image.filepath_from_user() != paths[name]):
                print(bpy.data.images[name].filepath_from_user())
                print(paths[name])
                image.filepath = paths[name]
                image.reload()
