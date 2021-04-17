from .points2D import Points2D


class Line2D(Points2D):

    def __init__(self, points):
        super().__init__(points)

    def getPoints(self):
        ret = []
        for p in self._points:
            ret.append(p.getPosition())
        return ret
    

    def getSection(self, index):
        ret = []
        ret.extend(self._points[index].getPosition())
        ret.extend(self._points[index+1].getPosition())
        return ret


    def printPoints(self):
        print(self._points.__len__())
        for p in self._points:
            print(p)


    def __str__(self):
        return str(self.getPoints())