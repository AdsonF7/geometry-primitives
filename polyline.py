class Polyline:
    
    def __init__(self):
        self.__points = []

    def AddPoint(self, point):
        self.__points.append(point)

    @property
    def Points(self):
        return self.__points
