import dash
from dash.dependencies import Input, Output
import dash_table
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import http.client
import json
#data=readDate("Assets\CSVFile\Taux_Pollution_Descartes.csv")

conn = http.client.HTTPSConnection("airdecartes.herokuapp.com")
payload = ''
headers = {}
conn.request("GET", "/AllCapteurData", payload, headers)
res = conn.getresponse()
datares = res.read()
df=pd.DataFrame(json.loads(datares.decode("utf-8")))

#df = pd.read_csv('Assets\CSVFile\Taux_Pollution_Descartes.csv')



TableMoM=html.Div([


    dash_table.DataTable(
        id='datatable-interactivity',


        sort_action="native",
        sort_mode="multi",

        selected_columns=[],
        selected_rows=[],
        page_action="native",
        page_current= 0,
        page_size= 10,
        style_header={
            'backgroundColor': 'rgb(133 113 48)',
            'fontWeight': 'bold'
        },

        style_data_conditional=[
            {
                'if': {
                    'column_id': '2',

                },
             'font-size':"20px",
            'padding-left':'20px',
            'backgroundColor': 'rgb(133 113 48);',
            'color': 'black',
            }]
    ),
    html.Div(id='datatable-interactivity-container')
])




