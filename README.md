# Which area a point is?

# Usage example
curl -X POST -H "Content-type: application/json" --data '{
	"epsg": 4326,
	"point": {"type": "Point","coordinates": [-47.88274, -15.79377]},
	"areas": [
		{
			"name": "rodoviaria_do_plano-terminal",
			"geometry": {"type":"Polygon","coordinates":[[[-47.88152,-15.7933],[-47.88212,-15.795],
							[-47.88388,-15.79444],[-47.88334,-15.79271],[-47.88152,-15.7933]],
							[[-47.88337,-15.79357],[-47.88318,-15.79363],[-47.88323,-15.79377],
							[-47.88341,-15.7937],[-47.88337,-15.79357]]]}
		}, {
			"name": "other_area",
			"geometry": {"type":"MultiPolygon","coordinates":[[...]]}
		}
	]
}' http://127.0.0.1:5000/

# Linux install

pip install shapely

pip install geopandas

pip install flask

# Windows install

pip install wheels

pip install pipwin

pip install flask

pipwin install numpy

pipwin install pandas

pipwin install shapely

pipwin install gdal

pipwin install fiona

pipwin install pyproj

pipwin install six

pipwin install rtree

pipwin install geopandas

# Run
Execute Flask with .bat or .sh scripts.
