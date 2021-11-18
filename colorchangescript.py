import maya.cmds as cmds

def changeColor():
    cmds.setAttr ('objSel' + ".overrideEnabled", 1)
    cmds.setAttr ('objSel' + ".overrideColor", 13)
    
def createControl():
    objSel=cmds.ls(sl=True)
    cmds.circle (n='ctrl')
    cmds.group ('ctrl',name='ctrlGroup')
    cmds.matchTransform('ctrlGroup',objSel)


def renameFunc(string):
    listObj = cmds.ls(selection=True)
    string.partition("##")
    for count, object in enumerate(listObj):
        cmds.rename(object, string.partition('#')[0] + str(count + 1).zfill(string.count('#')) + string.rpartition('#')[2])
renameFunc("Arm_##_Jnt")
changeColor()

