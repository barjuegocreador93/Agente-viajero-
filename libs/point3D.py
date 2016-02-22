#@autor: Camilo Barbosa

#Point3D
class Point3D:
    
    def __init__(self,X=0.0,Y=0.0,Z=0.0):
        self.X=X
        self.Y=Y
        self.Z=Z
    def Set(self,x=0.0,y=0.0,z=0.0):
        self.X=x
        self.Y=y
        self.Z=z
    def Draw(self):
        print "(",self.X ,",",self.Y , ",",self.Z,")"
    def USet(self):
        self.X,self.Y,self.Z=input("Enter x,y,z: ")
#Line3D
class Line3D:
    
    def __init__(self,A=Point3D(),B=Point3D()):
        self.A=A
        self.B=B
        self.d=0.0 #distans
        self.mp=Point3D() #medial point
        self.dv=Point3D() #directional Vector
    def SetLine(self,pointB,pointA=Point3D()):
        self.A=pointA
        self.B=pointB
    def DirectionalVector(self):
        dx=self.B.X-self.A.X
        dy=self.B.Y-self.A.Y
        dz=self.B.Z-self.A.Z
        self.dv.Set(dx,dy,dz)
        return self.dv
    def Distans(self):
        self.DirectionalVector()
        self.d=abs(pow(pow(self.dv.X,2)+pow(self.dv.Y,2)+pow(self.dv.Z,2),0.5))
        return self.d


