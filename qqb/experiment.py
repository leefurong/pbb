from app import App, Circle, Space
import pymunk
from pymunk import Vec2d

class PinJoint:
    def __init__(self, b, b2, a=(0, 0), a2=(0, 0)):
        joint = pymunk.constraint.PinJoint(b, b2, a, a2)
        space.add(joint)

app = App()
space = Space("两个小球撞来撞去")



b0 = space.static_body
p = Vec2d(200, 190)
v = Vec2d(80, 0)

c = Circle(p+v)
PinJoint(b0, c.body, p)

c2 = Circle(p+2*v)
PinJoint(b0, c2.body, p)

app.run()