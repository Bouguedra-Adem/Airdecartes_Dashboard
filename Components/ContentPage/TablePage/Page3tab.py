import dash_core_components as dcc
import dash_bootstrap_components as dbc
from .TableHt.table import tabhtml
import http.client
import json
import pandas as pd


containerpage3=dbc.Container([
     dbc.Row([dbc.Button("Refresh Data", outline=False, color="secondary", className="mr-1", id="refersh" )]),
     dbc.Row(
        [
             dbc.Col([tabhtml],lg=12,className="ColFiltre",id="ad"),

        ],
       id="Rowtabb"
     )],

    id="containerTab2",
fluid=True
)