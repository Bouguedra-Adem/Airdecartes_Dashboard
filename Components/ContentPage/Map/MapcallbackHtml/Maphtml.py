from datetime import date
import dash
import dash_html_components as html
import dash_core_components as dcc
import dash_bootstrap_components as dbc
import dash_leaflet as dl
import dash_leaflet.express as dlx
from dash import Dash, html
import pandas as pd
import re
import http.client
import json
#data=readDate("Assets\CSVFile\Taux_Pollution_Descartes.csv")

conn = http.client.HTTPSConnection("airdecartes.herokuapp.com")
payload = ''
headers = {}
conn.request("GET", "/AllCapteurData", payload, headers)
res = conn.getresponse()
datares = res.read()
data=pd.DataFrame(json.loads(datares.decode("utf-8")))
print(data[["lat","lng"]])
df=data

from dash_extensions.javascript import assign

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

# data = pd.read_csv("Assets\CSVFile\Taux_Pollution_Descartes.csv")
# print([dict(lat=float( row["Latitude"]), lon=float(row["Longitude"]))]  for index,row in data.iterrows())
colorscale = ['green', 'yellow', 'red']  # rainbow
chroma = "https://cdnjs.cloudflare.com/ajax/libs/chroma-js/2.1.0/chroma.min.js"  # js lib used for colors
color_prop = 'co2'
df = df[['lat', 'lng', 'address', color_prop]]  # drop irrelevant columns
dicts = df.to_dict('rows')
for item in dicts:
    item["tooltip"] = "{} ({:.1f})".format(item['address'], item[color_prop])  # bind tooltip
geojson = dlx.dicts_to_geojson(dicts, lon="lng")  # convert to geojson
geobuf = dlx.geojson_to_geobuf(geojson)  # convert to geobuf
vmax = df[color_prop].max()
colorbar = dl.Colorbar(colorscale=colorscale, width=20, height=150, min=0, max=vmax, unit='/km2')

point_to_layer = assign("""function(feature, latlng, context){
        const {min, max, colorscale, circleOptions, colorProp} = context.props.hideout;
        const csc = chroma.scale(colorscale).domain([min, max]);  // chroma lib to construct colorscale
        circleOptions.fillColor = csc(feature.properties[colorProp]);  // set color based on color prop.
        return L.circleMarker(latlng, circleOptions);  // sender a simple circle marker.
    }""")

geojson = dl.GeoJSON(data=geobuf, id="geojson", format="geobuf",
                         zoomToBounds=True,  # when true, zooms to bounds when data changes
                         options=dict(pointToLayer=point_to_layer),  # how to draw points
                         superClusterOptions=dict(radius=50),  # adjust cluster size
                         hideout=dict(colorProp=color_prop,
                                      circleOptions=dict(fillOpacity=0.7, stroke=False, radius=15),
                                      min=0, max=vmax, colorscale=colorscale))

#Map=html.Div([html.P('Dash converts Python classes into HTML')],id="divMap"  )





Map= html.Div([dl.Map([dl.TileLayer(),
                       dl.GeoJSON(data=geobuf, id="geojson", format="geobuf",
                         zoomToBounds=True,  # when true, zooms to bounds when data changes
                         options=dict(pointToLayer=point_to_layer),  # how to draw points
                         superClusterOptions=dict(radius=50),  # adjust cluster size
                         hideout=dict(colorProp=color_prop,circleOptions=dict(fillOpacity=0.7, stroke=False, radius=15),
                        min=0, max=vmax, colorscale=colorscale)),
                        colorbar],
                       center=(48.848298, 2.566190), zoom=13,style={'width': '100%', 'height': '900px', 'margin': "auto", "display": "block"})])




