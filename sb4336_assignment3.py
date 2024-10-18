maya.standalone.uninitialize()

import maya.standalone
import maya.cmds as cmds
import argparse

maya.standalone.initialize()

def create_sphere():
cmds.polySphere(name='mySphere', radius=8)
print("Sphere created.")

def create_cube():
cmds.polyCube(name='myCube', width=7, height=7, depth=7)
print("Cube created.")

def main(shape):
if shape == 'sphere':
create_sphere()
elif shape == 'cube':
create_cube()
else:
print("Invalid shape. Use 'sphere' or 'cube'.")

if **name** == "**main**":
parser = argparse.ArgumentParser(description="Create shapes in Maya.")
parser.add_argument('shape', choices=['sphere', 'cube'], help="Specify the shape to create.")
args = parser.parse_args()
main(args.shape)

maya.standalone.uninitialize()