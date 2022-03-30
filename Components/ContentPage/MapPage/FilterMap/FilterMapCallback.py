import dash_html_components as html
import dash
import datetime as date
import pandas as pd
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output
from callbacks_managers import CallbackManager
import dash_leaflet as dl
import dash_leaflet.express as dlx
from ast import literal_eval
import http.client
import json
from dash_extensions.javascript import assign

callback_managerFiltreMap = CallbackManager()

#data=readDate("Assets\CSVFile\Taux_Pollution_Descartes.csv")





@callback_managerFiltreMap.callback(
    dash.dependencies.Output("geojson", 'data')
    ,
    [
     dash.dependencies.Input('my-date-picker-rangeMap', 'start_date'),
     dash.dependencies.Input('my-date-picker-rangeMap', 'end_date'),

    ])

def update_output(start_date, end_date):
    conn = http.client.HTTPSConnection("airdecartes.herokuapp.com")
    payload = ''
    headers = {}
    conn.request("GET", "/AllCapteurData", payload, headers)
    res = conn.getresponse()
    datares = res.read()
    data = pd.DataFrame(json.loads(datares.decode("utf-8")))

    if ((start_date is not None) & ( end_date is not None)) :


        data['Dt']=pd.to_datetime(data['yearobservation'].astype(int).astype(str)+"-"+data['monthobservation'].astype(int).astype(str)+"-"+data['dayobservation'].astype(int).astype(str)).dt.strftime("%Y-%m-%d")

        print(data['Dt'])

        data['DtAxis'] ="Date_" +data['yearobservation'].astype(int).astype(str) + "-" + data['monthobservation'].astype(int).astype(str)

        start_date_object = pd.to_datetime(start_date).strftime("%Y-%m-%d")
        print(start_date_object)

        end_date_object = pd.to_datetime(end_date).strftime("%Y-%m-%d")
        data=data[(data['Dt'] <= end_date_object) & (data['Dt'] >=start_date_object) ]
        data=data.sort_values(by=["Dt"])
        print ( data)

        return MapFilterFunction (data)
        #return fig, columns, df, heatmap
        df=data
        external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

        return  data#MapFilterFunction(data)
    else :
        data['Dt'] = pd.to_datetime(
            data['yearobservation'].astype(int).astype(str) + "-" + data['monthobservation'].astype(int).astype(str) +"-"+
            data['dayobservation'].astype(int).astype(str)).dt.strftime("%Y-%m-%d")
        data['DtAxis'] = "Date_" + data['yearobservation'].astype(int).astype(str) + "-" + data[
            'monthobservation'].astype(int).astype(str)

        start_date_object = pd.to_datetime(start_date)

        end_date_object = pd.to_datetime(end_date)
        data = data[(data['Dt'] <= end_date_object) & (data['Dt'] >= start_date_object)]
        data = data.sort_values(by=["Dt"])
        print(data)
        #return fig, columns, df,heatmap
        return data#MapFilterFunction(data)


def MapFilterFunction (df) :
    '''
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

    return #html.Div([dl.MapPage([dl.TileLayer(), geojson, colorbar], center=(48.848298, 2.566190), zoom=13,style={'width': '100%', 'height': '900px', 'margin': "auto", "display": "block"})])
    '''
    color_prop="co2"
    df = df[['lat', 'lng', 'address', color_prop]]  # drop irrelevant columns
    dicts = df.to_dict('rows')
    for item in dicts:
        item["tooltip"] = "{} ({:.1f})".format(item['address'], item[color_prop])  # bind tooltip
    geojson = dlx.dicts_to_geojson(dicts, lon="lng")  # convert to geojson
    geobuf = dlx.geojson_to_geobuf(geojson)  # convert to geobuf
    return geobuf
