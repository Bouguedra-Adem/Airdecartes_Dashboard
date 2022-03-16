import dash_core_components as dcc
import dash_bootstrap_components as dbc
from .Histogram.Histogram import *

from .TableMoM.MoMTableHtml import *
from .Filtre_Hist_MoM.FiltreHTML import *

containerpage1=dbc.Container([

     dbc.Row(
        [
             dbc.Col([FiltreHistMoM],lg=12,className="ColFiltre",id="ad"),



             dbc.Col(
                 dbc.Col(hist,md=12,lg=12)
             ),


        ],
       id="Row1"
     ),
    dbc.Row(
        [
             dbc.Col([

                 html.Div([dcc.Dropdown( options=[
                       {'label': 'Co2 MoM', 'value': 'co2'},
                       {'label': 'Humidity MoM', 'value': 'humidity'},
                       {'label': 'Pression MoM', 'value': 'pression'},
                   ],value='co2',id='demo-dropdown')],style={"width": "20%"})
             ],className="DropDowClass"),


             dbc.Col([dbc.Col(TableMoM,lg=12)]
            ,className="DataTable",lg=12),

        ],
       id="Row2"
     )

],
    id="containerTab",
fluid=True
)