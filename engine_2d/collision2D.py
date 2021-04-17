from .matrixOp import Matrix_op
from .shape2D import Shape2D

class Collision:

    def intersection_point(self, l1, l2):
        x1 = l1[0][0]
        y1 = l1[0][1]
        x2 = l1[1][0]
        y2 = l1[1][1]
        x3 = l2[0][0]
        y3 = l2[0][1]
        x4 = l2[1][0]
        y4 = l2[1][1]

        matrix_tool = Matrix_op()
        dx1 = matrix_tool.determinant(
            [[matrix_tool.determinant([[x1,x2],[y1,y2]]), matrix_tool.determinant([[x3,x4], [y3,y4]])]
            ,[matrix_tool.determinant([[x1,x2],[1,1]]), matrix_tool.determinant([[x3,x4],[1,1]])]])

        dx2 = matrix_tool.determinant(
            [[matrix_tool.determinant([[x1,x2],[1,1]]), matrix_tool.determinant([[x3,x4], [1,1]])]
            ,[matrix_tool.determinant([[y1,y2],[1,1]]), matrix_tool.determinant([[y3,y4],[1,1]])]])

        dy1 = matrix_tool.determinant(
            [[matrix_tool.determinant([[x1,x2],[y1,y2]]), matrix_tool.determinant([[x3,x4], [y3,y4]])]
            ,[matrix_tool.determinant([[y1,y2],[1,1]]), matrix_tool.determinant([[y3,y4],[1,1]])]])

        dy2 = matrix_tool.determinant(
            [[matrix_tool.determinant([[x1,x2],[1,1]]), matrix_tool.determinant([[x3,x4], [1,1]])]
            ,[matrix_tool.determinant([[y1,y2],[1,1]]), matrix_tool.determinant([[y3,y4],[1,1]])]])

        px = dx1/dx2
        py = dy1/dy2

        return [px,py]
    
    def intersects(self, l1, l2):
        x1 = l1[0][0]
        y1 = l1[0][1]
        x2 = l1[1][0]
        y2 = l1[1][1]
        x3 = l2[0][0]
        y3 = l2[0][1]
        x4 = l2[1][0]
        y4 = l2[1][1]

        a = x2 - x1
        b = x4 - x3
        c = x3 - x1
        d = y2 - y1
        e = y4 - y3
        f = y3 - y1

        tem_d = (a*e-b*d)

        if tem_d == 0:
            return False

        t = (c*d - a*f)/tem_d
        
        

        if a == 0:
            s = (f + e*t)/d
        else:
            s = (c + b*t)/a

        if s>=0 and s <= 1 and t <= 1 and t >= 0 :
            #print(str(a)+" "+str(b)+" "+str(c)+" "+str(d)+" "+str(e)+" "+str(f))
            #print(str(s)+" "+str(t))
            return True
        else:
            return False

    def intersects_at(self, l1, l2):
        x1 = l1[0][0]
        y1 = l1[0][1]
        x2 = l1[1][0]
        y2 = l1[1][1]
        x3 = l2[0][0]
        y3 = l2[0][1]
        x4 = l2[1][0]
        y4 = l2[1][1]

        a = x2 - x1
        b = x4 - x3
        c = x3 - x1
        d = y2 - y1
        e = y4 - y3
        f = y3 - y1

        tem_d = (a*e-b*d)

        if tem_d == 0:
            return False

        t = (c*d - a*f)/tem_d
        
        

        if a == 0:
            s = (f + e*t)/d
        else:
            s = (c + b*t)/a

        if s>=0 and s <= 1 and t <= 1 and t >= 0 :
            return [x1 + (x2-x1)*s, y1 + (y2-y1)*s]
        else:
            return False

    def shapesCollision(self, s1:Shape2D, s2:Shape2D):
        s1Points = s1.getLinesToDraw()
        s2Points = s2.getLinesToDraw()

        for p1 in s1Points:
            for p2 in s2Points:
                res = self.intersects_at(p1, p2)
                if res != False:
                   return res
        return False


