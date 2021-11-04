import maya.cmds as cmds

def renameFunc(string):
    listObj = cmds.ls(selection=True)
    string.partition("##")
    for count, object in enumerate(listObj):
        cmds.rename(object, string.partition('#')[0] + str(count + 1).zfill(string.count('#')) + string.rpartition('#')[2])

renameFunc("Arm_##_Jnt")
