import pybullet as p
import os


class slippyPlane:
    def __init__(self, client):
        f_name = os.path.join(os.path.dirname(__file__), 'slippyPlane.urdf')
        p.loadURDF(fileName=f_name,
                   basePosition=[0, 0, 0],
                   physicsClientId=client)

