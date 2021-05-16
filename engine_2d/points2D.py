from .vector2D import Vector2D 

class Points2D:

    def __init__(self, points):
        self._points = []
        for point in points:
            self._points.append(Vector2D(point))
        
    
    def move(self, v):
        for i in range(0, self._points.__len__()):
            self._points[i].move(v)

    def scale(self, scale):
        for i in range(0, len(self._points)):
            self._points[i] = self._points[i]*scale

    
