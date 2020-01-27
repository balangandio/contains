from geometry import Geometry


class Area:

    def __init__(self, name: str, area: Geometry):
        if area.type != 'Polygon' and area.type != 'MultiPolygon':
            raise ValueError('Area geometry type not Polygon or MultiPolygon')
        self._name = name
        self.area = area

    @property
    def name(self):
        return self._name

    @property
    def geometry(self):
        return self.area

    def boundary_distance(self, point: Geometry) -> float:
        area = self.area.to_crs('epsg:31983')
        point = point.to_crs('epsg:31983')
        return area.boundary.distance(point)

    def contains(self, other: Geometry) -> bool:
        area = self.area.to_crs('epsg:31983')
        other = other.to_crs('epsg:31983')
        return area.contains(other)

    def representation(self) -> dict:
        to_str = dict()
        to_str['name'] = self.name
        to_str['epsg_code'] = self.area.epsg_code
        to_str['geometry'] = self.geometry.to_geojson()
        return to_str

    def __repr__(self):
        return str(self.representation())
