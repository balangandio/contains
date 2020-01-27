from shapely.geometry.base import BaseGeometry
from geopandas.geodataframe import GeoDataFrame
from shapely.geometry import shape
from geopandas import GeoSeries
import json


class Geometry:

    def __init__(self, geometry: BaseGeometry, epsg_code: str):
        self.geometry = geometry
        self._epsg_code = epsg_code

    @property
    def geo(self) -> BaseGeometry:
        return self.geometry

    @property
    def type(self) -> str:
        return self.geometry.type

    @property
    def epsg_code(self) -> str:
        return self._epsg_code

    def to_crs(self, epsg_to: str) -> BaseGeometry:
        if self.epsg_code == epsg_to:
            return self.geo
        gdf = GeoDataFrame(crs=self.epsg_code, geometry=[self.geo])
        return gdf.to_crs(epsg_to).geometry.values[0]

    def to_geojson(self) -> dict:
        return json.loads(GeoSeries([self.geo]).to_json())['features'][0]['geometry']

    @staticmethod
    def from_geojson(geojson: dict, epsg_code: str):
        return Geometry(shape(geojson), epsg_code)
