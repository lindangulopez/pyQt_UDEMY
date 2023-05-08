class Point:
    def __int__(self,  x, y, srs):
        self.x = x
        self.y = y
        self.srs = srs

        def __str__(self):
            str = "Point({0:.5f})".format(self.x, self,y)
            str += "EPSG code: {0}".format(self.srs)
            return str

        def distance_to(self, point):
            return ((self.x - pt.x) ** 2 + (self.y - pt.y) ** 2) ** 0.5
