import maya.cmds as cmds


def changeColor():
    colorSel = cmds.ls(sl=True)
    cmds.setAttr(colorSel[0] + ".overrideEnabled", 1)
    cmds.setAttr(colorSel[0] + ".overrideColor", 13)


def createControl():
    objsel = cmds.ls(sl=True)
    for obj in objsel:
        circle = cmds.circle(n='ctrl')
        group = cmds.group(circle, name='GroupJnt')
        cmds.matchTransform(group, obj)
    print(objSel)



def renameFunc(string):
    objSel = cmds.ls(selection=True)
    string.partition("##")
    for count, object in enumerate(objSel):
        cmds.rename(object,
                    string.partition('#')[0] + str(count + 1).zfill(string.count('#')) + string.rpartition('#')[2])


createControl()
cmds.select("GroupJnt")
renameFunc("Arm_##_Ctrl_Grp")
cmds.select("ctrl")
renameFunc("Arm_##_Ctrl")
cmds.select("Arm_##_Ctrl")
changeColor()



