import maya.cmds as cmds

def changeColor()
crvSel = cmds.ls(sl=true)
cmds.setAttr(crvSel + ".overrideEnabled", 1)
cmds.setAttr(crvSel + "overrideRGBColors", 0)
cmds.optionMenu(omenu, q=True, v=True)
val=cDict.get(key, 0)
cmds.setAttr(crvSel + ".overrideColor", val)

changeColor()
