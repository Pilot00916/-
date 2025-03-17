import math
class Segment:
    def __init__(self, first_point, second_point):
        self.first_point = first_point
        self.second_point = second_point

    def length(self):
        x1, y1 = self.first_point
        x2, y2 = self.second_point
        return round(math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2), 2)

    def x_axis_intersection(self):
        _, y1 = self.first_point
        _, y2 = self.second_point
        return (y1 <= 0 <= y2) or (y2 <= 0 <= y1)

    def y_axis_intersection(self):
        x1, _ = self.first_point
        x2, _ = self.second_point
        return (x1 <= 0 <= x2) or (x2 <= 0 <= x1)
