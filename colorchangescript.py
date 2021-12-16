import maya.cmds as cmds



def ChangeColor(color):
    sels = cmds.ls(sl=True)
    for sel in sels:
        shapes = cmds.listRelatives(sel, children=True, shapes=True)
        for shape in shapes:
            cmds.setAttr('%s.overrideEnabled' % (shape), True)
            cmds.setAttr('%s.overrideColor' % (shape), color)
    return
  
    
def createControl():
    objsel = cmds.ls(selection=True)
    for obj in objsel:
        circle = cmds.circle (n='ctrl')
        ctrlgroup = cmds.group (circle,name='GroupJnt##')
        cmds.matchTransform(ctrlgroup,obj)
    print(objsel)
    
    


def renameFunc(string):
    objSel = cmds.ls(selection=True)
    string.partition("##")
    for count, object in enumerate(objSel):
        cmds.rename(object, string.partition('#')[0] + str(count + 1).zfill(string.count('#')) + string.rpartition('#')[2])

createControl()
cmds.select("GroupJnt**")
renameFunc("Arm_##_Ctrl_Grp")
cmds.select("ctrl*")
ChangeColor(13)
renameFunc("Arm_##_Ctrl")

    
    
