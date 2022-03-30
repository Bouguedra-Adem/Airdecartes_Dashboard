import dash_html_components as html
import dash
import datetime as date
import pandas as pd
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output, State
from callbacks_managers import CallbackManager
import dash_leaflet as dl
import dash_leaflet.express as dlx
from ast import literal_eval
import http.client
import json
from dash_extensions.javascript import assign

def getdata() :
    conn = http.client.HTTPSConnection("airdecartes.herokuapp.com")
    payload = ''
    headers = {}
    conn.request("GET", "/AllCapteurData", payload, headers)
    res = conn.getresponse()
    datares = res.read()
    data=pd.DataFrame(json.loads(datares.decode("utf-8")))
    data['Date'] = pd.to_datetime( data['yearobservation'].astype(int).astype(str) + "-" + data['monthobservation'].astype(int).astype(str) + "-" + data['dayobservation'].astype(int).astype(str)).dt.strftime("%d-%b-%Y")

    data = data[["codecapteur", "Date", "temperature", "co2", "pression", "humidity", "lat", "lng", "address"]]
    return  data


callback_managerFiltretab = CallbackManager()


@callback_managerFiltretab.callback(
    Output('datatable-interactivity1', 'style_data_conditional'),
    Input('datatable-interactivity1', 'selected_columns')
)
def update_styles(selected_columns):
    return [{
        'if': { 'column_id': i },
        'background_color': '#D2F3FF'
    } for i in selected_columns]

@callback_managerFiltretab.callback(

        Output("datatable-interactivity1", "data"),


    [Input("refersh", "n_clicks")],

)
def UpdateTabe( nclick):

    print("adeeeeeeeeeeeeeeeeeeee")
    return getdata().to_dict('records')
