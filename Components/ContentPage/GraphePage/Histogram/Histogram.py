
import dash_core_components as dcc
import dash_bootstrap_components as dbc
from numpy import array

from .HistogramData import *
import plotly.graph_objects as go
import dash_html_components as html
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



animals=['giraffes', 'orangutans', 'monkeys']



histt=html.Div([
    go.Figure([go.Bar(x=animals, y=[20, 14, 23])])
])



hist=dcc.Graph(
        id='example-graph',
        className="Histogram",
        figure={
            'data': [{'name': 'temperature',
              'type': 'bar',
              'x': array(['Date_2022-1', 'Date_2022-2', 'Date_2022-3', 'Date_2022-4',
                          'Date_2022-5'], dtype=object),
              'y': [866, 1292, 1331, 1370, 1036]},
             {'name': 'co2',
              'type': 'bar',
              'x': array(['Date_2022-1', 'Date_2022-2', 'Date_2022-3', 'Date_2022-4',
                          'Date_2022-5'], dtype=object),
              'y': [17117, 24367, 24406, 24445, 18432]},
             {'name': 'pression',
              'type': 'bar',
              'x': array(['Date_2022-1', 'Date_2022-2', 'Date_2022-3', 'Date_2022-4',
                          'Date_2022-5'], dtype=object),
              'y': [780, 1336, 1375, 1414, 1038]},
             {'name': 'humidity',
              'type': 'bar',
              'x': array(['Date_2022-1', 'Date_2022-2', 'Date_2022-3', 'Date_2022-4',
                          'Date_2022-5'], dtype=object),
              'y': [1496, 2142, 2181, 2220, 1647]}],
    'layout': {'barmode': 'stack', 'template': '...', 'xaxis': {'categoryorder': 'category ascending'}}

        }

    )

dbc.Container(
    dbc.Row([
        dbc.Col(),

    ])
)

