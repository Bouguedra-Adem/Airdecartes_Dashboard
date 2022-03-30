
from dash import Dash, dash_table, dcc, html
from dash.dependencies import Input, Output
import pandas as pd
import http.client
import json

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


df=getdata()
tabhtml = html.Div([
    dash_table.DataTable(
        id='datatable-interactivity1',
        columns=[
            {"name": i, "id": i, "deletable": True, "selectable": True} for i in df.columns
        ],
        data=getdata().to_dict('records'),

        filter_action="native",
        sort_action="native",
        sort_mode="multi",
        row_selectable="multi",
        selected_rows=[],
        page_action="native",
        page_current= 0,
        page_size= 10,

    ),
    html.Div(id='datatable-interactivity-container')
],id="tab")

