import maya.cmds as cmds


## changes color of wireframes and nurbs

def ChangeColor(color):
    sels = cmds.ls(sl=True)
    for sel in sels:
        shapes = cmds.listRelatives(sel, children=True, shapes=True)
        for shape in shapes:
            cmds.setAttr('%s.overrideEnabled' % (shape), True)
            cmds.setAttr('%s.overrideColor' % (shape), color)
    return
    
## Sequential renamer

def renameFunc(string):
    objSel = cmds.ls(selection=True)
    string.partition("##")
    for count, object in enumerate(objSel):
        cmds.rename(object, string.partition('#')[0] + str(count + 1).zfill(string.count('#')) + string.rpartition('#')[2])

## creates a control and control group, matches its transforms to the geometry. 
def createControl():
    objsel = cmds.ls(selection=True)
    for obj in objsel:
        circle = cmds.circle (n='ctrl')
        ctrlgroup = cmds.group (circle,name='GroupJnt##')
        cmds.matchTransform(ctrlgroup,obj)
    print(objsel)

