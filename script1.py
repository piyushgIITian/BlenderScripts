##### please select the dst mesh in the object mode tab before running this script


## import neccessary modules
import bpy, os

##set blender context
context = bpy.context

##set source and destination objects,  you can also load them dynamically using blender import scene ops.
src_obj = context.scene.objects['F_Body.001']
dst_obj = context.scene.objects['F_Body.003']

## for exporting the entire object
dst_obj_armature = bpy.data.objects['Armature.027']

## find shapekeys in source object
keyBlocks = src_obj.data.shape_keys.key_blocks

## iterate shapekeys based on index
for ind in reversed(range(len(keyBlocks))):
    ## clear dst_obj shape keys if u want single shapekey per export
    dst_obj.shape_key_clear()
    ## setting it false so that shapkey_transfer function doesnt get confused
    dst_obj_armature.select_set(False)

    ## src is set true first because it has shapekeys
    src_obj.select_set(True)
    dst_obj.select_set(True)
    
    src_obj.active_shape_key_index = ind
    bpy.ops.object.shape_key_transfer()

    ## for exporting dst obj
    src_obj.select_set(False)
    dst_obj_armature.select_set(True)
    
    ## you can use export options as per your choices refer here for more info https://docs.blender.org/api/current/bpy.ops.export_scene.html
    
    bpy.ops.export_scene.gltf(filepath='shapeKeys/'+keyBlocks[ind].name+'.gltf',use_selection=True,export_format='GLTF_EMBEDDED',export_materials='EXPORT',export_image_format='NONE')
    
