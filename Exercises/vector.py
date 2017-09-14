#! /usr/bin/env python3
class Vector:

    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
    
    def __str__(self):
        return "(" + str(self.x) + ", " + str(self.y) + ", " + str(self.z) + ")"

v1 = Vector(1, 2, 3)
v2 = Vector(5, 6, 7)

print(v1)
print(v2)

#print(v1 + v2) #should print (6, 8, 10)
#print(v1 - v2) #should print (-4, -4, -4)
#print(v1 * v2) #should print 38
