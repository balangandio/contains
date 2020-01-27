from typing import List
from area import Area
from geometry import Geometry
from functools import reduce


class Model:

    def __init__(self, areas: List[Area]):
        self.areas = areas

    def select_area(self, point: Geometry) -> Area:
        areas = self.witch_ones_contains(point)

        if len(areas) == 0:
            return None

        condition = lambda prev_area, next_area: prev_area if prev_area[1] > next_area[1] else next_area

        areas_bondaries = [(area, area.boundary_distance(point)) for area in areas]

        return reduce(condition, areas_bondaries)[0]

    def witch_ones_contains(self, other: Geometry) -> List[Area]:
        return [area for area in self.areas if area.contains(other)]
