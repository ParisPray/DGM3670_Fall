import maya.cmds as cmds

##def changeColor():
    ##objSel = cmds.ls(selection=True)
    ##cmds.setAttr ('objSel' + ".overrideEnabled", 0)
    ##cmds.setAttr ('objSel' + ".overrideColor", 13)
def changeColor():
    colorSel = cmds.ls(sl=True)
    cmds.setAttr ('colorSel' + ".overrideEnabled", 0)
    cmds.setAttr ('colorSel' + ".overrideColor", 13)
    
    
def createControl():
    cmds.circle (n='ctrl')
    objSel = cmds.ls(selection=True)
    cmds.group ('ctrl',name='GroupJnt')
    cmds.matchTransform('GroupJnt',objSel)


def renameFunc(string):
    objSel = cmds.ls(selection=True)
    string.partition("##")
    for count, object in enumerate(objSel):
        cmds.rename(object, string.partition('#')[0] + str(count + 1).zfill(string.count('#')) + string.rpartition('#')[2])

createControl()
cmds.select ("ctrl*")
renameFunc("Arm_##_Jnt")
cmds.select("GoupJnt")
renameFunc("Arm_##_Grp")

