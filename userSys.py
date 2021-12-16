import sys
import maya.cmds as cmds
print(sys.path)



## opens port for connection to python
if not cmds.commandPort(":4434", query=True):
    cmds.commandPort(name=":4434")

## Please make sure the directory path is correct in order for access to modules. 

if r"C:\Users\paris\Documents\GitKraken\DGM3670Fall_Scripting\DGM3670_Fall" not in sys.path:
    sys.path.append(r"C:\Users\paris\Documents\GitKraken\DGM3670Fall_Scripting\DGM3670_Fall")
    cmds.commandPort(name="5535")
    
    
    
    
    
    
    
for s in sys.path:
    print(s)