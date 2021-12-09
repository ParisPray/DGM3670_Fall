import maya.cmds as cmds


class ToolUI():
    def __init__(self):
        self.m_window = 'changeColorUIWin'

    def create(self):
        self.delete()

        self.m_window = cmds.window(self.m_window,
                                    title="Big Chungus",
                                    widthHeight=(200, 55))
        m_column = cmds.columnLayout(parent=self.m_window,
                                     adjustableColumn= False)
        cmds.button(parent=m_column, label='Ball', command='cmds.polySphere()')
        cmds.button(parent=m_column, w=25, h=10, bgc= (255, 0, 0), command=lambda x: changeColor(13))

        cmds.showWindow(self.m_window)

        ##def show(self):
        ##cmds.showWindow(self.m_window)
        ##if cmds.window(self.m_window, exists=True):
       ##     cmds.deleteUI(self.m_window)  ##

    def delete(self):
        if cmds.window(self.m_window, exists=True):
            cmds.deleteUI(self.m_window)



myUI= ToolUI()
myUI.create()


def changeColor(color):
    sels = cmds.ls(sl=True)
    for sel in sels:
        shapes = cmds.listRelatives(sel, children=True, shapes=True)
        for shape in shapes:
            cmds.setAttr('%s.overrideEnabled' % (shape), True)
            cmds.setAttr('%s.overrideColor' % (shape), color)
    return
