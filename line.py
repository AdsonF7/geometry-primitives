class Line:

    def __init__(self, start_point=None, end_point=None):
        self.__start_point = start_point
        self.__end_point = end_point

    @property
    def StartPoint(self):
        return self.__start_point

    @property
    def EndPoint(self):
        return self.__end_point

    @StartPoint.setter
    def StartPoint(self, value):
        self.__start_point = value

    @EndPoint.setter
    def EndPoint(self, value):
        self.__end_point = value
