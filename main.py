from geometry import Geometry
from area import Area
from model import Model
from flask import Flask, request


class Service:

    @staticmethod
    def select_area(epsg_code: str, areas_json: [dict], point_json: dict) -> dict:
        epsg_code = 'epsg:' + epsg_code
        areas = [Area(json['name'], Geometry.from_geojson(json['geometry'], epsg_code)) for json in areas_json]
        point = Geometry.from_geojson(point_json, epsg_code)

        selected_area = Model(areas).select_area(point)

        selected_area.boundary_distance(point)

        if selected_area is None:
            return None

        return {
            'selected_area': selected_area.representation(),
            'boundary_distance': selected_area.boundary_distance(point)
        }


app = Flask(__name__)


@app.route('/', methods=['POST', 'GET'])
def determinate():
    if request.method == 'GET':
        return {
            'message': 'unaspected usage',
            'correct_usage': {
                'method': 'POST',
                'parameters': {
                    'epsg': 'EPSG code that geometry objects came from',
                    'areas': [
                        {
                            'name': 'identification name',
                            'geometry': 'Polygon or MultiPolygon geojson geometry'
                        }
                    ],
                    'point': 'Geojson geometry that identifies a point'
                },
                'example': {
                    'epsg': 4326,
                    'point': {"type": "Point","coordinates": [-47.88274, -15.79377]},
                    'areas': [
                        {
                            "name": "rodoviaria_do_plano-terminal",
                            "geometry": {"type": "Polygon", "coordinates": [[[-47.88152, -15.7933], [-47.88212, -15.795], [-47.88388, -15.79444], [-47.88334, -15.79271], [-47.88152, -15.7933]], [[-47.88337, -15.79357], [-47.88318, -15.79363], [-47.88323, -15.79377], [-47.88341, -15.7937], [-47.88337, -15.79357]]]}
                        }, {
                            "name": "rodoviaria_do_plano-area",
                            "geometry": {"type": "MultiPolygon", "coordinates": [[[[-47.88324, -15.79471], [-47.88277, -15.79484], [-47.8823, -15.79497], [-47.88237, -15.79519], [-47.88215, -15.79526], [-47.8806, -15.79572], [-47.88048, -15.79583], [-47.88028, -15.79589], [-47.8803, -15.79593], [-47.87977, -15.79608], [-47.87966, -15.79577], [-47.88184, -15.79509], [-47.88178, -15.79489], [-47.88142, -15.79385], [-47.88138, -15.79379], [-47.88133, -15.79375], [-47.88129, -15.79373], [-47.88122, -15.79372], [-47.88118, -15.79373], [-47.88116, -15.79368], [-47.88115, -15.79366], [-47.88072, -15.79375], [-47.88069, -15.79375], [-47.88054, -15.79366], [-47.88049, -15.7936], [-47.87962, -15.79388], [-47.87954, -15.79364], [-47.87956, -15.79364], [-47.87956, -15.79362], [-47.88006, -15.79348], [-47.8805, -15.79334], [-47.88059, -15.79357], [-47.88073, -15.79367], [-47.88079, -15.79361], [-47.88083, -15.79359], [-47.88097, -15.79352], [-47.88117, -15.79344], [-47.88115, -15.79338], [-47.88165, -15.7932], [-47.88168, -15.79319], [-47.88161, -15.793], [-47.88178, -15.79294], [-47.88184, -15.79312], [-47.88279, -15.79278], [-47.88363, -15.79248], [-47.88368, -15.79254], [-47.88386, -15.79247], [-47.88409, -15.7924], [-47.88427, -15.79241], [-47.88445, -15.79248], [-47.88465, -15.7926], [-47.88488, -15.79283], [-47.88502, -15.79315], [-47.88508, -15.79344], [-47.88504, -15.79374], [-47.88502, -15.79386], [-47.88491, -15.79406], [-47.88478, -15.79419], [-47.88462, -15.79428], [-47.88448, -15.79433], [-47.8844, -15.79442], [-47.88324, -15.79471]]]]}
                        }
                    ]
                }
            }
        }

    json = request.json
    epsg_code = str(json['epsg'])
    areas = json['areas']
    point = json['point']

    return Service.select_area(epsg_code, areas, point)
