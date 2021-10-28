import maya.cmds as cmds

cmds.polySphere(sx=50, sy=50, r=20)
cmds.move( 0, 1, 0 )

cmds.polySphere(sx=50, sy=50, r=12)
cmds.move( 0, 25, 0 )

cmds.polySphere(sx=50, sy=50, r=7)
cmds.move( 0, 40, 0 )

cmds.polyCylinder(sx=20, sy=20, r=10, h=1)
cmds.move( -2,43,0)
cmds.rotate(0,0,25)

cmds.polyCylinder(sx=50, sy=20, r=6, h=5)
cmds.move( -3,46,0)
cmds.rotate(0,0,25)

cmds.polyCylinder(sx=20, sy=20, r=0.5, h=20)
cmds.move( 0,30,11.5)
cmds.rotate(60,0,0)

cmds.polyCylinder(sx=20, sy=20, r=0.5, h=20)
cmds.move( 0,30,-11.5)
cmds.rotate(-60,0,0)

cmds.polyCylinder(sx=20, sy=20, r=0.25, h=5)
cmds.move( 0,35,-17)
cmds.rotate(-18.5,0,0)

cmds.polyCylinder(sx=20, sy=20, r=0.25, h=5)
cmds.move( 0,34.2,-17.5)
cmds.rotate(-43,0,0)

cmds.polyCylinder(sx=20, sy=20, r=0.25, h=5)
cmds.move( 0,35,17)
cmds.rotate(18.5,0,0)

cmds.polyCylinder(sx=20, sy=20, r=0.25, h=5)
cmds.move( 0,34.2,17.5)
cmds.rotate(43,0,0)

cmds.polyCylinder(sx=20, sy=20, r=1, h=1)
cmds.move( 5.4,42.8,3.3)
cmds.rotate(-29.3,5.5,107.85)

cmds.polyCylinder(sx=20, sy=20, r=1, h=1)
cmds.move( 5.4,42.8,-3.3)
cmds.rotate(32.1,5.5,107.85)

cmds.polyCone( sx=20, sy=20, sz=20, r=1, h=5)
cmds.move(8.3,42.4,0)
cmds.rotate(0,0,-70)

cmds.polyCylinder(sx=20, sy=20, r=0.75, h=1)
cmds.move(5.5,38.8,-3.3)
cmds.rotate(29,14.9,91.74)

cmds.polyCylinder(sx=20, sy=20, r=0.75, h=1)
cmds.move(6.5,38.3,-0.6)
cmds.rotate(11,14.9,91.74)

cmds.polyCylinder(sx=20, sy=20, r=0.75, h=1)
cmds.move(6.3,38.6,2.1)
cmds.rotate(-11,14.9,91.74)