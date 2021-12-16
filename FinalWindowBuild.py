import sys
import maya.cmds as cmds
import tools



class ToolUI():
    def __init__(self):
        self.m_window = 'changeColorUIWin'
        self.m_grid = "main_grid"

    def create(self):
        self.delete()

        self.m_window = cmds.window(self.m_window,
                                    title="Control Creator",
                                    widthHeight=(200, 55))

        m_column = cmds.columnLayout(columnAttach=('both', 5), columnWidth=500, parent=self.m_window)

        cmds.text(label="Color Index", parent=m_column, font="boldLabelFont")
        m_grid = cmds.gridLayout(parent=self.m_window, numberOfColumns=6)

## Color Index Buttons ##
        cmds.button(label='0', parent=m_grid, w=25, h=25, bgc=(0.1, .1, .1), command=lambda x: tools.ChangeColor(0))
        cmds.button(label='1', parent=m_grid, w=25, h=25, bgc=(0, 0, 0), command=lambda x: tools.ChangeColor(1))
        cmds.button(label='2', parent=m_grid, w=25, h=25, bgc=(.15, .15, .15), command=lambda x: tools.ChangeColor(2))
        cmds.button(label='3', parent=m_grid, w=25, h=25, bgc=(.30, .30, .30), command=lambda x: tools.ChangeColor(3))
        cmds.button(label='4', parent=m_grid, w=25, h=25, bgc=(.4, .1, .1), command=lambda x: tools.ChangeColor(4))
        cmds.button(label='5', parent=m_grid, w=25, h=25, bgc=(.1, .1, .4), command=lambda x: tools.ChangeColor(5))
        cmds.button(label='6', parent=m_grid, w=25, h=25, bgc=(.25, .35, .55), command=lambda x: tools.ChangeColor(6))
        cmds.button(label='7', parent=m_grid, w=25, h=25, bgc=(.1, .3, .1), command=lambda x: tools.ChangeColor(7))
        cmds.button(label='8', parent=m_grid, w=25, h=25, bgc=(.1, .02, .2), command=lambda x: tools.ChangeColor(8))
        cmds.button(label='9', parent=m_grid, w=25, h=25, bgc=(.65, .4, .7), command=lambda x: tools.ChangeColor(9))
        cmds.button(label='10', parent=m_grid, w=25, h=25, bgc=(.45, .3, .2), command=lambda x: tools.ChangeColor(10))
        cmds.button(label='11', parent=m_grid, w=25, h=25, bgc=(.2, .1, 0.1), command=lambda x: tools.ChangeColor(11))
        cmds.button(label='12', parent=m_grid, w=25, h=25, bgc=(.4, .15, 0.15), command=lambda x: tools.ChangeColor(12))
        cmds.button(label='13', parent=m_grid, w=25, h=25, bgc=(1, 0, 0), command=lambda x: tools.ChangeColor(13))
        cmds.button(label='14', parent=m_grid, w=25, h=25, bgc=(0, 1, 0), command=lambda x: tools.ChangeColor(14))
        cmds.button(label='15', parent=m_grid, w=25, h=25, bgc=(0, 0, 1), command=lambda x: tools.ChangeColor(15))
        cmds.button(label='16', parent=m_grid, w=25, h=25, bgc=(1, 1, 1), command=lambda x: tools.ChangeColor(16))
        cmds.button(label='17', parent=m_grid, w=25, h=25, bgc=(1, 1, 0), command=lambda x: tools.ChangeColor(17))
        cmds.button(label='18', parent=m_grid, w=25, h=25, bgc=(.6, .8, 1), command=lambda x: tools.ChangeColor(18))
        cmds.button(label='19', parent=m_grid, w=25, h=25, bgc=(.6, 1, .8), command=lambda x: tools.ChangeColor(19))
        cmds.button(label='20', parent=m_grid, w=25, h=25, bgc=(1, .8, .8), command=lambda x: tools.ChangeColor(20))
        cmds.button(label='21', parent=m_grid, w=25, h=25, bgc=(1, .8, .5), command=lambda x: tools.ChangeColor(21))
        cmds.button(label='22', parent=m_grid, w=25, h=25, bgc=(.9, .9, .5), command=lambda x: tools.ChangeColor(22))
        cmds.button(label='23', parent=m_grid, w=25, h=25, bgc=(.5, .8, .5), command=lambda x: tools.ChangeColor(23))
        cmds.button(label='24', parent=m_grid, w=25, h=25, bgc=(.5, .4, .1), command=lambda x: tools.ChangeColor(24))
        cmds.button(label='25', parent=m_grid, w=25, h=25, bgc=(.5, .5, .1), command=lambda x: tools.ChangeColor(25))
        cmds.button(label='26', parent=m_grid, w=25, h=25, bgc=(.4, .5, .1), command=lambda x: tools.ChangeColor(26))
        cmds.button(label='27', parent=m_grid, w=25, h=25, bgc=(.3, .5, .4), command=lambda x: tools.ChangeColor(27))
        cmds.button(label='28', parent=m_grid, w=25, h=25, bgc=(.3, .5, .5), command=lambda x: tools.ChangeColor(28))
        cmds.button(label='29', parent=m_grid, w=25, h=25, bgc=(.3, .4, .6), command=lambda x: tools.ChangeColor(29))
        cmds.button(label='30', parent=m_grid, w=25, h=25, bgc=(.35, .2, .6), command=lambda x: tools.ChangeColor(30))
        cmds.button(label='31', parent=m_grid, w=25, h=25, bgc=(.6, .2, .5), command=lambda x: tools.ChangeColor(31))
## creates the Create Control Button. 
        cmds.text(label="", parent=m_column)
        cmds.button(label='Create Control', parent=m_column, w=25, h=25, command=lambda x: tools.createControl())
## creates the Rename text field and Rename function button
        cmds.text(label="", parent=m_column)

        self.rename_textfield = cmds.textFieldButtonGrp(parent=m_column, label='Rename', placeholderText="Arm_##_Grp",
                                                        buttonLabel='Apply', buttonCommand=lambda *x: tools.renameFunc(cmds.textFieldButtonGrp(self.rename_textfield,q=True, text = True)))

        cmds.showWindow(self.m_window)

    

    def delete(self):
        if cmds.window(self.m_window, exists=True):
            cmds.deleteUI(self.m_window)
            



myUI = ToolUI()
myUI.create()




